import re

def normalize_phone(phone_number):
    # Remove all characters except digits and '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Check if the number has an international code
    if not cleaned_number.startswith('+'):
        # Add '+38' if the number does not start with an international code
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number

    return cleaned_number

# Example usage
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS-mailing:", sanitized_numbers)
