import sys
import os

def fetch_lines(file_path):
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, file_path)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if not line.startswith('#')]
            return lines
    except Exception as error:
        print("Failed to open file:")
        print(error)
        sys.exit(1)

def display_error(message, line_number):
    print(f"\n{message} at line {line_number}")
    sys.exit(1)

def get_user_input(prompt):
    return input(f"{prompt}: ")

def interprett(file_path):
    commands = fetch_lines(file_path)

    for line_number, line in enumerate(commands):
        elements = line.split(" ")
        command = elements[0]

        if command == "FLIP":
            user_input = get_user_input("Enter something to reverse")
            flipped_input = user_input[::-1]
            print(flipped_input)

        elif command == "DUPLICATE":
            symbol = get_user_input("Enter a character(s) to repeat")
            count = int(get_user_input("Enter the number of times to repeat the character"))
            print(symbol * count)

        elif command == "COMBINE":
            first_number = int(get_user_input("first number:"))
            second_number = int(get_user_input("second number:"))
            total = first_number * second_number
            print(total)

        elif command == "SHOW":
            if len(elements) < 2:
                display_error("Error: SHOW command needs an argument", line_number)
            print(" ".join(elements[1:]))

        elif command == "VOICE":
            print(get_user_input("Enter something to printout"))

        

        

def run():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    #interprett(os.path.join(current_directory, "HelloW.txt"))
    #interprett(os.path.join(current_directory, "reverse.txt"))
    interprett(os.path.join(current_directory, "multiply.txt"))
    #interprett(os.path.join(current_directory, "repeat.txt"))

if __name__ == "__main__":
    run()