import datetime
import time
import re

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
        
        # Calculate months and days (approximation for simplicity without external libs)
        # Create a date object for the birthday in the current year
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
    # Using current time for simplicity, or could ask user for start time
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
    # Note: Python's zoneinfo is best for this, but requires Python 3.9+ or tzdata.
    # We will use simple fixed offsets for compatibility.
    
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        
        current_offset = float(input("Enter your current timezone offset (e.g., -5 for EST, 5.5 for IST): "))
        target_offset = float(input("Enter target timezone offset (e.g., 9 for JST, 0 for UTC): "))
        
        # Logic: Convert to UTC first, then to target
        current_tz = datetime.timezone(datetime.timedelta(hours=current_offset))
        target_tz = datetime.timezone(datetime.timedelta(hours=target_offset))
        
        # Set current info
        dt = dt.replace(tzinfo=current_tz)
        
        # Convert
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
            # If time passed today, assume tomorrow
            target_dt += datetime.timedelta(days=1)
            
        print(f"Counting down to {target_dt} (Press Ctrl+C to stop)...")
        
        while True:
            now = datetime.datetime.now()
            remaining = target_dt - now
            
            if remaining.total_seconds() <= 0:
                print("\nTime's up!")
                break
                
            # Formatting the output to stay on one line
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
    # Basic regex for email validation
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
    
    # Remove any non-digit characters first
    clean_phone = re.sub(r"\D", "", phone)
    
    if len(clean_phone) == 10:
        # Capture groups: (3 digits) (3 digits) (4 digits)
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
    
    # \b ensures we match whole words only, re.IGNORECASE for case insensitivity
    matches = re.findall(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE)
    
    print(f"Found '{word}' {len(matches)} times.")

# ==========================================
# 10. Date Extractor
# ==========================================
def date_extractor():
    print("\n--- Date Extractor ---")
    text = input("Enter text containing dates (e.g., 'Due on 2023-10-15 or 15/10/2023'): ")
    
    # Matches YYYY-MM-DD or DD/MM/YYYY
    # Pattern explanation:
    # \d{4}-\d{2}-\d{2}  -> Matches 2023-10-05
    # \d{2}/\d{2}/\d{4}  -> Matches 05/10/2023
    pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
    
    dates = re.findall(pattern, text)
    
    if dates:
        print("Dates found:", dates)
    else:
        print("No dates found in supported formats.")

# ==========================================
# Main Menu
# ==========================================
def main():
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
        elif choice == '0': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
