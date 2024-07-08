from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Convert the birthday string to a datetime.date object
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        
        # Adjust the birthday year to the current year
        birthday_this_year = birthday.replace(year=today.year)
        
        # Check if the birthday has already passed this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate the difference in days
        days_until_birthday = (birthday_this_year - today).days
        
        # If the birthday is within the next 7 days
        if days_until_birthday <= 7:
            # Check if the birthday falls on a weekend
            if birthday_this_year.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
                # Move the congratulation date to the next Monday
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            
            # Append the result to the list
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.07.07"},
    {"name": "Jane Smith", "birthday": "1990.07.13"},
    {"name": "Tom Hanks", "birthday": "1956.07.09"},  
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of congratulations for this week:", upcoming_birthdays)
