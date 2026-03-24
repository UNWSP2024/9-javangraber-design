# Programmer: Javan Graber
# Date: 3/24/2026
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

# Import the random module
import random

def create_random_number_file():
    # Create the random number file
    random_number_file = open('random_number_file.txt', 'w')

    # Ask for the number of random numbers
    try:
        print('How many random numbers do you want in the file?')
        number_of_numbers = int(input('Enter the number (at least 1 but no greater than 1000): '))

    except ValueError:
        print('Make sure to only enter an integer!')
        number_of_numbers = int(input('Enter the number (at least 1 but no greater than 1000): '))

    # Create a loop that ensures the needed range is followed
    if number_of_numbers < 1 or number_of_numbers > 1000:
        print("Please enter a number at least 1 but no greater than 1000")
        number_of_numbers = int(input("Enter the number: "))

    # Create a loop that generates the random numbers in the range
    # of 1 to 500 and adds them to the file
    for number in range(number_of_numbers):
        random_number = random.randint(1, 500)
        random_number_file.write(f'{random_number}\n')

    # Close the file
    random_number_file.close()

    # Print that the file was created
    print("A file has been made according to your requirements.")

# Call the main function
if __name__ == '__main__':
    create_random_number_file()
