import random

def get_numbers_ticket(min, max, quantity):
    # Validate the input parameters
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Generate a set of unique random numbers
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min, max))
    
    # Convert the set to a sorted list and return
    return sorted(unique_numbers)

# Examples of function call
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 5, 5)
print("Your lottery numbers:", lottery_numbers)
