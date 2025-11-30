import threading
import math
import os
import time
from collections import Counter

# ========================================================
# EXERCISE 1: THREADED PRIME NUMBER CHECKER
# ========================================================

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_worker(start, end, result_list, lock):
    """
    Worker function for threads.
    Finds primes in a sub-range and appends them to a shared list safely.
    """
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    
    # Critical Section: Use lock to safely write to the shared list
    with lock:
        result_list.extend(local_primes)

def run_prime_exercise(limit=100, num_threads=4):
    print(f"\n--- Exercise 1: Finding Primes up to {limit} with {num_threads} threads ---")
    
    primes_found = []
    thread_lock = threading.Lock()
    threads = []
    
    # Calculate chunk size (how many numbers each thread checks)
    chunk_size = limit // num_threads
    
    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size + 1
        # Ensure the last thread covers the remainder of the range
        end = limit + 1 if i == num_threads - 1 else (i + 1) * chunk_size + 1
        
        t = threading.Thread(target=prime_worker, args=(start, end, primes_found, thread_lock))
        threads.append(t)
        t.start()
        print(f"Started Thread-{i+1} for range [{start}, {end})")

    # Wait for all threads to complete
    for t in threads:
        t.join()
        
    end_time = time.time()

    # Sort results because threads might finish in random order
    primes_found.sort()
    
    print(f"\nTotal Primes Found: {len(primes_found)}")
    print(f"Primes: {primes_found}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")


# ========================================================
# EXERCISE 2: THREADED FILE PROCESSING
# ========================================================

def create_dummy_file(filename="large_text_file.txt"):
    """Creates a file with sample text for testing."""
    if not os.path.exists(filename):
        content = "python threading is powerful " * 50 + "\n"
        content += "homework is fun when code works " * 50 + "\n"
        content += "apple banana cherry date elderberry " * 50 + "\n"
        
        # Replicating content to make it 'large'
        with open(filename, "w") as f:
            for _ in range(100): 
                f.write(content)
        print(f"\n[Setup] Created dummy file: {filename}")

def word_count_worker(lines, index, thread_results):
    """
    Worker function.
    Counts words in a specific list of lines.
    Stores the result in a specific index of the results list.
    """
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    
    # Store local result; no lock needed as we write to a unique index
    thread_results[index] = local_counter

def run_file_processing_exercise(filename="large_text_file.txt", num_threads=4):
    print(f"\n--- Exercise 2: Counting Words in '{filename}' ---")
    
    # 1. Read the file
    try:
        with open(filename, 'r') as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        print("File not found. Please run setup first.")
        return

    # 2. Split lines among threads
    total_lines = len(all_lines)
    chunk_size = math.ceil(total_lines / num_threads)
    
    threads = []
    # A list to store results from each thread (index-based storage avoids locking)
    thread_results = [None] * num_threads 

    start_time = time.time()

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, total_lines)
        
        # Slice the lines for this thread
        lines_chunk = all_lines[start_idx:end_idx]
        
        t = threading.Thread(target=word_count_worker, args=(lines_chunk, i, thread_results))
        threads.append(t)
        t.start()

    # 3. Join threads
    for t in threads:
        t.join()

    # 4. Merge results
    final_counter = Counter()
    for result in thread_results:
        final_counter.update(result)

    end_time = time.time()

    print(f"Total Unique Words: {len(final_counter)}")
    print(f"Top 5 Most Common Words: {final_counter.most_common(5)}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")


# ========================================================
# MAIN EXECUTION
# ========================================================

if __name__ == "__main__":
    # Run Exercise 1
    run_prime_exercise(limit=100, num_threads=4)

    # Setup and Run Exercise 2
    create_dummy_file()
    run_file_processing_exercise()
    
    # Cleanup (Optional)
    # os.remove("large_text_file.txt")
