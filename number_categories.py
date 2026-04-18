# Function to get odd numbers
def get_odds(numbers):
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds

# Function to get even numbers
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Function to get prime numbers
def get_primes(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            # Manually check for factors
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Main Program
user_numbers = []
print("Enter 10 numbers:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Number {i+1}: "))
            user_numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Process and Print
odds = get_odds(user_numbers)
evens = get_evens(user_numbers)
primes = get_primes(user_numbers)

print("\nResults:")
print("Odds:", odds if odds else "None found")
print("Evens:", evens if evens else "None found")
print("Primes:", primes if primes else "None found")
