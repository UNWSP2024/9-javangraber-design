# Programmer: Javan Graber
# Date: 3/24/2026
# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    ######################
    # Prepare for an IOError exception
    try:
        # Open the numbers.txt file for reading
        sum_file = open('numbers.txt', 'r')

        # Set an accumulator equal to 0
        total = 0

        # Create a loop that converts each line to an integer and adds them to the total
        for line in sum_file:
            number_to_add = int(line)
            total += number_to_add

        # Close the file
        sum_file.close()

        # Print the total
        print(f"The sum of the numbers is: {total}")

    # Prepare for the exceptions
    except IOError:
        #Display an error message
        print("File not found")

    except ValueError:
        print("All items must be integers")
    ######################

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
