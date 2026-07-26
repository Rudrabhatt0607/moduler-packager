

import datetime
import math
import random
import string
import time
import uuid
import importlib

import file_ops  # custom module (file_ops.py must be in the same folder)


SEPARATOR = "=" * 27


def pause_and_show(choice_prompt="\nEnter your choice: "):
    return input(choice_prompt)



# 1. DATETIME AND TIME OPERATIONS

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(SEPARATOR)

        elif choice == "2":
            d1 = input("\nEnter the first date (YYYY-MM-DD): ")
            d2 = input("Enter the second date (YYYY-MM-DD): ")
            try:
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                diff = abs((date2 - date1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
            print(SEPARATOR)

        elif choice == "3":
            fmt = input("\nEnter a custom format (e.g. %d/%m/%Y %H:%M:%S): ")
            try:
                print(f"Formatted Date: {datetime.datetime.now().strftime(fmt)}")
            except ValueError:
                print("Invalid format string.")
            print(SEPARATOR)

        elif choice == "4":
            input("\nPress Enter to start the stopwatch...")
            start = time.time()
            input("Stopwatch running... Press Enter to stop.")
            elapsed = time.time() - start
            print(f"Elapsed Time: {elapsed:.2f} seconds")
            print(SEPARATOR)

        elif choice == "5":
            try:
                seconds = int(input("\nEnter countdown time (in seconds): "))
                while seconds > 0:
                    print(seconds, end="\r")
                    time.sleep(1)
                    seconds -= 1
                print("Time's up!            ")
            except ValueError:
                print("Please enter a valid integer.")
            print(SEPARATOR)

        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")



# 2. MATHEMATICAL OPERATIONS
def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                n = int(input("\nEnter a number: "))
                print(f"Factorial: {math.factorial(n)}")
            except ValueError:
                print("Please enter a valid non-negative integer.")
            print(SEPARATOR)

        elif choice == "2":
            try:
                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                amount = p * (1 + r / 100) ** t
                ci = amount - p
                print(f"Compound Interest: {ci:.2f}")
            except ValueError:
                print("Please enter valid numeric values.")
            print(SEPARATOR)

        elif choice == "3":
            try:
                angle = float(input("\nEnter angle in degrees: "))
                rad = math.radians(angle)
                print(f"sin({angle}) = {math.sin(rad):.4f}")
                print(f"cos({angle}) = {math.cos(rad):.4f}")
                print(f"tan({angle}) = {math.tan(rad):.4f}")
            except ValueError:
                print("Please enter a valid number.")
            print(SEPARATOR)

        elif choice == "4":
            print("\n1. Circle  2. Rectangle  3. Triangle")
            shape = input("Choose a shape: ")
            try:
                if shape == "1":
                    r = float(input("Enter radius: "))
                    print(f"Area: {math.pi * r ** 2:.2f}")
                elif shape == "2":
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    print(f"Area: {l * w:.2f}")
                elif shape == "3":
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))
                    print(f"Area: {0.5 * b * h:.2f}")
                else:
                    print("Invalid shape choice.")
            except ValueError:
                print("Please enter valid numeric values.")
            print(SEPARATOR)

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")



# 3. RANDOM DATA GENERATION

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                low = int(input("\nEnter lower bound: "))
                high = int(input("Enter upper bound: "))
                print(f"Random Number: {random.randint(low, high)}")
            except ValueError:
                print("Please enter valid integers.")
            print(SEPARATOR)

        elif choice == "2":
            try:
                size = int(input("\nEnter list size: "))
                low = int(input("Enter lower bound: "))
                high = int(input("Enter upper bound: "))
                print(f"Random List: {[random.randint(low, high) for _ in range(size)]}")
            except ValueError:
                print("Please enter valid integers.")
            print(SEPARATOR)

        elif choice == "3":
            try:
                length = int(input("\nEnter password length: "))
                chars = string.ascii_letters + string.digits + string.punctuation
                password = "".join(random.choice(chars) for _ in range(length))
                print(f"Generated Password: {password}")
            except ValueError:
                print("Please enter a valid integer.")
            print(SEPARATOR)

        elif choice == "4":
            try:
                length = int(input("\nEnter OTP length: "))
                otp = "".join(random.choice(string.digits) for _ in range(length))
                print(f"Generated OTP: {otp}")
            except ValueError:
                print("Please enter a valid integer.")
            print(SEPARATOR)

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")



# 4. GENERATE UNIQUE IDENTIFIERS (UUID)

def uuid_menu():
    print("\nGenerate Unique Identifiers:")
    print(f"Generated UUID: {uuid.uuid4()}")
    print(SEPARATOR)


# 5. FILE OPERATIONS (CUSTOM MODULE)

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("\nEnter file name: ")
            if file_ops.create_file(filename):
                print("File created successfully!")
            else:
                print("Could not create file.")
            print(SEPARATOR)

        elif choice == "2":
            filename = input("\nEnter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_file(filename, data)
            print("Data written successfully!")
            print(SEPARATOR)

        elif choice == "3":
            filename = input("\nEnter file name: ")
            content = file_ops.read_file(filename)
            if content is None:
                print("File not found.")
            else:
                print("File Content:")
                print(content)
            print(SEPARATOR)

        elif choice == "4":
            filename = input("\nEnter file name: ")
            data = input("Enter data to append: ")
            file_ops.append_file(filename, data)
            print("Data appended successfully!")
            print(SEPARATOR)

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")



# 6. EXPLORE MODULE ATTRIBUTES (dir())

def explore_module():
    print("\nExplore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    try:
        mod = importlib.import_module(module_name)
        attrs = [a for a in dir(mod) if not a.startswith("_")]
        print(f"Available Attributes in {module_name} module:")
        print(attrs)
    except ImportError:
        print(f"Module '{module_name}' not found.")
    print(SEPARATOR)



# MAIN MENU

def main():
    while True:
        print(SEPARATOR)
        print("Welcome to Multi-Utility Toolkit")
        print(SEPARATOR)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print(SEPARATOR)
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print(SEPARATOR)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(SEPARATOR)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
