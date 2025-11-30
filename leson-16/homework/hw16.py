import datetime
import time
import re
import json
import requests
import random
import os
import sqlite3
import numpy as np

# ==========================================
# Helper: Create Dummy Files for JSON Tasks
# ==========================================
def setup_dummy_files():
    if not os.path.exists("students.json"):
        data = [
            {"id": 1, "name": "Alice Smith", "grade": "A", "age": 20},
            {"id": 2, "name": "Bob Jones", "grade": "B", "age": 22},
            {"id": 3, "name": "Charlie Brown", "grade": "A-", "age": 21}
        ]
        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)
            
    if not os.path.exists("books.json"):
        data = [
            {"id": 101, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
            {"id": 102, "title": "1984", "author": "George Orwell"}
        ]
        with open("books.json", "w") as f:
            json.dump(data, f, indent=4)

# ==========================================
# 1. Age Calculator
# ==========================================
def age_calculator():
    print("\n--- Age Calculator ---")
    dob_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
        today = datetime.date.today()
        
        # Calculate years
        years = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            years -= 1
        
        # Calculate months and days (approximation)
        this_year_bday = datetime.date(today.year, dob.month, dob.day)
        if this_year_bday > today:
            this_year_bday = datetime.date(today.year - 1, dob.month, dob.day)
            
        delta = today - this_year_bday
        months = delta.days // 30
        days = delta.days % 30
        
        print(f"You are approximately {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# ==========================================
# 2. Days Until Next Birthday
# ==========================================
def days_until_birthday():
    print("\n--- Days Until Next Birthday ---")
    dob_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
        today = datetime.date.today()
        
        # Determine next birthday
        next_bday = dob.replace(year=today.year)
        if next_bday < today:
            next_bday = dob.replace(year=today.year + 1)
            
        days_remaining = (next_bday - today).days
        print(f"There are {days_remaining} days until your next birthday!")
    except ValueError:
        print("Invalid date format.")

# ==========================================
# 3. Meeting Scheduler
# ==========================================
def meeting_scheduler():
    print("\n--- Meeting Scheduler ---")
    start_str = input("Enter meeting start time (YYYY-MM-DD HH:MM) or press Enter for Now: ")
    
    if start_str.strip() == "":
        start_time = datetime.datetime.now()
    else:
        try:
            start_time = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format.")
            return

    try:
        duration_h = int(input("Enter duration (hours): "))
        duration_m = int(input("Enter duration (minutes): "))
        
        end_time = start_time + datetime.timedelta(hours=duration_h, minutes=duration_m)
        print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")
    except ValueError:
        print("Invalid number entered.")

# ==========================================
# 4. Timezone Converter
# ==========================================
def timezone_converter():
    print("\n--- Timezone Converter ---")
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        
        current_offset = float(input("Enter your current timezone offset (e.g., -5 for EST, 5.5 for IST): "))
        target_offset = float(input("Enter target timezone offset (e.g., 9 for JST, 0 for UTC): "))
        
        current_tz = datetime.timezone(datetime.timedelta(hours=current_offset))
        target_tz = datetime.timezone(datetime.timedelta(hours=target_offset))
        
        dt = dt.replace(tzinfo=current_tz)
        target_dt = dt.astimezone(target_tz)
        print(f"Time in target timezone: {target_dt.strftime('%Y-%m-%d %H:%M %z')}")
        
    except ValueError:
        print("Invalid input format.")

# ==========================================
# 5. Countdown Timer
# ==========================================
def countdown_timer():
    print("\n--- Countdown Timer ---")
    target_str = input("Enter target time (HH:MM:SS) for today: ")
    try:
        now = datetime.datetime.now()
        target_time = datetime.datetime.strptime(target_str, "%H:%M:%S").time()
        target_dt = datetime.datetime.combine(now.date(), target_time)
        
        if target_dt < now:
            target_dt += datetime.timedelta(days=1)
            
        print(f"Counting down to {target_dt} (Press Ctrl+C to stop)...")
        
        while True:
            now = datetime.datetime.now()
            remaining = target_dt - now
            
            if remaining.total_seconds() <= 0:
                print("\nTime's up!")
                break
            print(f"Time remaining: {str(remaining).split('.')[0]}", end="\r")
            time.sleep(1)
            
    except ValueError:
        print("Invalid format.")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

# ==========================================
# 6. Email Validator
# ==========================================
def email_validator():
    print("\n--- Email Validator ---")
    email = input("Enter an email address: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

# ==========================================
# 7. Phone Number Formatter
# ==========================================
def phone_number_formatter():
    print("\n--- Phone Number Formatter ---")
    phone = input("Enter 10-digit phone number (e.g., 1234567890): ")
    clean_phone = re.sub(r"\D", "", phone)
    
    if len(clean_phone) == 10:
        formatted = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", clean_phone)
        print(f"Formatted: {formatted}")
    else:
        print("Please enter exactly 10 digits.")

# ==========================================
# 8. Password Strength Checker
# ==========================================
def password_strength_checker():
    print("\n--- Password Strength Checker ---")
    pwd = input("Enter password: ")
    
    errors = []
    if len(pwd) < 8:
        errors.append("Must be at least 8 characters long.")
    if not re.search(r"[A-Z]", pwd):
        errors.append("Must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", pwd):
        errors.append("Must contain at least one lowercase letter.")
    if not re.search(r"\d", pwd):
        errors.append("Must contain at least one digit.")
        
    if not errors:
        print("Strong password!")
    else:
        print("Weak password:")
        for e in errors:
            print(f"- {e}")

# ==========================================
# 9. Word Finder
# ==========================================
def word_finder():
    print("\n--- Word Finder ---")
    text = input("Enter the text to search in: ")
    word = input("Enter the word to find: ")
    matches = re.findall(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE)
    print(f"Found '{word}' {len(matches)} times.")

# ==========================================
# 10. Date Extractor
# ==========================================
def date_extractor():
    print("\n--- Date Extractor ---")
    text = input("Enter text containing dates (e.g., 'Due on 2023-10-15 or 15/10/2023'): ")
    pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
    dates = re.findall(pattern, text)
    if dates:
        print("Dates found:", dates)
    else:
        print("No dates found in supported formats.")

# ==========================================
# 11. JSON Parsing (students.json)
# ==========================================
def json_parsing_task():
    print("\n--- JSON Parsing: Students ---")
    filename = "students.json"
    
    # Ensure file exists
    setup_dummy_files()
    
    try:
        with open(filename, 'r') as f:
            students = json.load(f)
            
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade'}")
        print("-" * 40)
        for s in students:
            print(f"{s.get('id', ''):<5} {s.get('name', ''):<20} {s.get('age', ''):<5} {s.get('grade', '')}")
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# ==========================================
# 12. Weather API
# ==========================================
def weather_api_task():
    print("\n--- Weather API ---")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    if not api_key:
        print("API Key is required.")
        return
        
    city = input("Enter city name (e.g., Tashkent): ").strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            
            print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Condition: {weather['description'].capitalize()}")
        else:
            print("City not found or Invalid API Key.")
    except Exception as e:
        print(f"Connection error: {e}")

# ==========================================
# 13. JSON Modification (books.json)
# ==========================================
def json_modification_task():
    print("\n--- JSON Modification: Books ---")
    filename = "books.json"
    setup_dummy_files()
    
    while True:
        print("\n[Book Menu] 1.List 2.Add 3.Update 4.Delete 5.Back")
        choice = input("Choice: ")
        
        # Reload data every time to ensure freshness
        try:
            with open(filename, 'r') as f:
                books = json.load(f)
        except:
            books = []

        if choice == '1':
            for b in books:
                print(f"ID: {b['id']} | {b['title']} by {b['author']}")
                
        elif choice == '2':
            try:
                new_id = int(input("Enter ID: "))
                title = input("Title: ")
                author = input("Author: ")
                books.append({"id": new_id, "title": title, "author": author})
                print("Book added.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '3':
            try:
                b_id = int(input("Enter Book ID to update: "))
                for b in books:
                    if b['id'] == b_id:
                        b['title'] = input(f"New title ({b['title']}): ") or b['title']
                        b['author'] = input(f"New author ({b['author']}): ") or b['author']
                        print("Book updated.")
                        break
                else:
                    print("ID not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '4':
            try:
                b_id = int(input("Enter Book ID to delete: "))
                initial_len = len(books)
                books = [b for b in books if b['id'] != b_id]
                if len(books) < initial_len:
                    print("Book deleted.")
                else:
                    print("ID not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            break
            
        # Save changes
        if choice in ['2', '3', '4']:
            with open(filename, 'w') as f:
                json.dump(books, f, indent=4)

# ==========================================
# 14. Movie Recommendation System
# ==========================================
def movie_recommendation_task():
    print("\n--- Movie Recommendation System ---")
    api_key = input("Enter your OMDb API Key: ").strip()
    if not api_key:
        print("API Key is required.")
        return

    # OMDb doesn't support "get random movie by genre" directly in free tier easily.
    # We will search for the genre name as a keyword to find relevant titles.
    genre_keyword = input("Enter a movie genre (e.g., Action, Comedy, Horror): ").strip()
    
    # Search for movies with this keyword
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre_keyword}&type=movie"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("Response") == "True":
            movies = data.get("Search", [])
            if movies:
                # Pick a random movie from the search results
                random_movie = random.choice(movies)
                title = random_movie.get("Title")
                year = random_movie.get("Year")
                imdb_id = random_movie.get("imdbID")
                
                print(f"\nRecommendation: {title} ({year})")
                
                # Optional: Fetch detailed info to confirm genre/plot
                detail_url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
                detail_resp = requests.get(detail_url).json()
                print(f"Plot: {detail_resp.get('Plot', 'N/A')}")
                print(f"IMDb Rating: {detail_resp.get('imdbRating', 'N/A')}")
            else:
                print("No movies found for that genre/keyword.")
        else:
            print(f"Error: {data.get('Error')}")
            
    except Exception as e:
        print(f"Connection error: {e}")

# ==========================================
# 15. Database Roster Task
# ==========================================
def database_roster_task():
    print("\n--- Database Roster Task ---")
    db_file = "roster.db"
    
    try:
        # Connect to database (creates it if it doesn't exist)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Drop table to ensure a fresh start for this homework exercise
        cursor.execute("DROP TABLE IF EXISTS Roster")
        
        # 1. Create Table
        cursor.execute("""
            CREATE TABLE Roster (
                Name TEXT,
                Species TEXT,
                Age INTEGER
            )
        """)
        print("Table 'Roster' created.")
        
        # 2. Populate Table
        people = [
            ("Benjamin Sisko", "Human", 40),
            ("Jadzia Dax", "Trill", 300),
            ("Kira Nerys", "Bajoran", 29)
        ]
        cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", people)
        print("Initial data inserted.")
        
        # 3. Update Name (Jadzia Dax -> Ezri Dax)
        cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
        print("Updated 'Jadzia Dax' to 'Ezri Dax'.")
        
        # 4. Display Bajorans
        print("\n--- Bajoran Crew Members ---")
        cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(f"Name: {row[0]}, Age: {row[1]}")
        else:
            print("No Bajorans found.")
            
        # Commit and close
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# ==========================================
# NumPy Exercises (Tasks 16-25)
# ==========================================

# 16. Convert List to 1D Array
def numpy_list_to_array():
    print("\n--- NumPy: List to 1D Array ---")
    original_list = [12.23, 13.32, 100, 36.32]
    print("Original List:", original_list)
    np_array = np.array(original_list)
    print("One-dimensional NumPy array:", np_array)

# 17. Create 3x3 Matrix (2-10)
def numpy_3x3_matrix():
    print("\n--- NumPy: 3x3 Matrix (2-10) ---")
    # Values 2 to 10 is 9 values, fits perfectly in 3x3
    matrix = np.arange(2, 11).reshape(3, 3)
    print(matrix)

# 18. Null Vector (Size 10) & Update 6th Value
def numpy_null_vector():
    print("\n--- NumPy: Null Vector & Update ---")
    null_vector = np.zeros(10)
    print("Original:", null_vector)
    
    # Updating 6th value (Index 6 based on sample output visualization, or Index 5 based on counting)
    # Sample output provided: [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.] -> Index 6 is the 7th element.
    # We will match the visual output provided in the homework.
    null_vector[6] = 11
    print("Update sixth value to 11:")
    print(null_vector)

# 19. Array from 12 to 38
def numpy_range_array():
    print("\n--- NumPy: Array 12 to 38 ---")
    arr = np.arange(12, 38)
    print(arr)

# 20. Convert Array to Float Type
def numpy_float_conversion():
    print("\n--- NumPy: Convert to Float ---")
    original = [1, 2, 3, 4]
    print("Original array:", original)
    as_float = np.asfarray(original)
    print("Float array:", as_float)

# 21. Celsius to Fahrenheit Conversion
def numpy_temp_conversion():
    print("\n--- NumPy: Temperature Conversion ---")
    # Sample data from homework (looks like Fahrenheit values based on output)
    sample_f = np.array([0, 12, 45.21, 34, 99.91])
    
    # Convert F to C: (F - 32) * 5/9
    centigrade = (sample_f - 32) * 5/9
    
    # Convert C to F (for completeness/verification): C * 9/5 + 32
    fahrenheit_back = (centigrade * 9/5) + 32
    
    print("Values in Fahrenheit degrees:")
    print(sample_f)
    print("Values in Centigrade degrees:")
    print(np.round(centigrade, 2))

# 22. Append Values to Array
def numpy_append_values():
    print("\n--- NumPy: Append Values ---")
    original = np.array([10, 20, 30])
    print("Original array:", original)
    
    # Appending values to create [10 20 30 40 50 60 70 80 90]
    to_append = [40, 50, 60, 70, 80, 90]
    new_arr = np.append(original, to_append)
    print("After append values to the end of the array:")
    print(new_arr)

# 23. Array Statistical Functions
def numpy_stats():
    print("\n--- NumPy: Statistics ---")
    # Random array of 10 elements
    arr = np.random.rand(10)
    print("Array:", arr)
    print(f"Mean: {np.mean(arr):.4f}")
    print(f"Median: {np.median(arr):.4f}")
    print(f"Std Dev: {np.std(arr):.4f}")

# 24. Find Min and Max (10x10)
def numpy_min_max():
    print("\n--- NumPy: Min/Max 10x10 ---")
    arr = np.random.random((10, 10))
    # print("Array:", arr) # Too large to print clearly
    print(f"Minimum Value: {arr.min()}")
    print(f"Maximum Value: {arr.max()}")

# 25. Create 3x3x3 Array
def numpy_3d_array():
    print("\n--- NumPy: 3x3x3 Array ---")
    arr = np.random.random((3, 3, 3))
    print(arr)

# ==========================================
# Main Menu
# ==========================================
def main():
    setup_dummy_files() # Ensure JSON files exist
    while True:
        print("\n==============================")
        print("   HOMEWORK MENU")
        print("==============================")
        print("1. Age Calculator")
        print("2. Days Until Next Birthday")
        print("3. Meeting Scheduler")
        print("4. Timezone Converter")
        print("5. Countdown Timer")
        print("6. Email Validator")
        print("7. Phone Number Formatter")
        print("8. Password Strength Checker")
        print("9. Word Finder")
        print("10. Date Extractor")
        print("--- API & DB Tasks ---")
        print("11. JSON Parsing (Students)")
        print("12. Weather API")
        print("13. JSON Modification (Books)")
        print("14. Movie Recommendation")
        print("15. Database Roster")
        print("--- NumPy Exercises ---")
        print("16. List to 1D Array")
        print("17. 3x3 Matrix (2-10)")
        print("18. Null Vector Update")
        print("19. Range 12-38")
        print("20. Convert to Float")
        print("21. Temp Conversion")
        print("22. Append Values")
        print("23. Statistics (Mean/Med/Std)")
        print("24. Min/Max (10x10)")
        print("25. 3x3x3 Array")
        print("0. Exit")
        
        choice = input("\nEnter exercise number: ")
        
        if choice == '1': age_calculator()
        elif choice == '2': days_until_birthday()
        elif choice == '3': meeting_scheduler()
        elif choice == '4': timezone_converter()
        elif choice == '5': countdown_timer()
        elif choice == '6': email_validator()
        elif choice == '7': phone_number_formatter()
        elif choice == '8': password_strength_checker()
        elif choice == '9': word_finder()
        elif choice == '10': date_extractor()
        elif choice == '11': json_parsing_task()
        elif choice == '12': weather_api_task()
        elif choice == '13': json_modification_task()
        elif choice == '14': movie_recommendation_task()
        elif choice == '15': database_roster_task()
        elif choice == '16': numpy_list_to_array()
        elif choice == '17': numpy_3x3_matrix()
        elif choice == '18': numpy_null_vector()
        elif choice == '19': numpy_range_array()
        elif choice == '20': numpy_float_conversion()
        elif choice == '21': numpy_temp_conversion()
        elif choice == '22': numpy_append_values()
        elif choice == '23': numpy_stats()
        elif choice == '24': numpy_min_max()
        elif choice == '25': numpy_3d_array()
        elif choice == '0': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
