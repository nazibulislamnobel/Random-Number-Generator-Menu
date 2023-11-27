import random

def generate_random_number(min, max):
    return random.randint(min, max)

def generate_random_even_number(min, max):
    number = generate_random_number(min, max)
    while number % 2 != 0:
        number = generate_random_number(min, max)
    return number

def generate_10_random_numbers(min, max):
    random_numbers = [generate_random_number(min, max) for _ in range(10)]
    return random_numbers

def generate_5_random_odd_numbers(min, max):
    random_odd_numbers = []
    total_sum = 0
    for _ in range(5):
        random_odd_number = generate_random_number(min, max)
        while random_odd_number % 2 == 0:
            random_odd_number = generate_random_number(min, max)
        random_odd_numbers.append(random_odd_number)
        total_sum += random_odd_number
    return random_odd_numbers, total_sum

def main():
    while True:
        print("Enter 1 to generate a random number between 1 and 100")
        print("Enter 2 to generate a random even number between 1 and 100")
        print("Enter 3 to generate 10 random numbers between 1 and 100")
        print("Enter 4 to generate 5 random odd numbers between 1 and 100 and print them with their sum")
        print("Enter 5 to exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            random_number = generate_random_number(1, 100)
            print("Random number between 1 and 100:", random_number)
        elif choice == 2:
            random_even_number = generate_random_even_number(1, 100)
            print("Random even number between 1 and 100:", random_even_number)
        elif choice == 3:
            random_numbers = generate_10_random_numbers(1, 100)
            print("10 random numbers:", random_numbers)
        elif choice == 4:
            random_odd_numbers, total_sum = generate_5_random_odd_numbers(1, 100)
            print("Random odd numbers and their sum:", random_odd_numbers, ", sum =", total_sum)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

main()