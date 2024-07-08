from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Get the current date
        today = datetime.today()
        
        # Calculate the difference between the current date and the input date
        delta = today - date_obj
        
        # Return the difference in days as an integer
        return delta.days
    except ValueError:
        # Handling the case of incorrect date format
        return "Invalid date format. Please use 'YYYY-MM-DD'."

# Examples of function call
print(get_days_from_today("2024-06-08"))
print(get_days_from_today("2024-07-12"))
print(get_days_from_today("2022/2/24"))
