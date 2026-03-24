# Programmer: Javan Graber
# Date: 3/24/2026
# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################

    # Create the original constant for the count
    count = 0
    try:
        # Open the file
        with open('names.txt', 'r') as count_file:

            # Create a for loop that counts every line and increases the original count
            for line in count_file:
                count += 1

    # Prepare for a IOError
    except IOError:

        # Print an error message
        print("The file could not be found")

    # Print the count
    print(f"There are {count} names in the names.txt file")
    ######################




# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
