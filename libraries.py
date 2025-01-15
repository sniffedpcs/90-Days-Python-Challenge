import math
from math import sqrt  # Importing specific function for convenience

def calculate_root():
    print("Square Root Calculator")
    
    try:
        # Get number from user
        number = float(input("Enter a number to find its square root: "))
        
        # Check if number is negative
        if number < 0:
            # math.sqrt() will raise an error for negative numbers
            # Let's also show how to find complex roots
            complex_root = math.sqrt(abs(number)) * 1j
            print(f"The square root of {number} is {complex_root}")
        else:
            # Calculate square root using different methods
            result_math = math.sqrt(number)    # Using math.sqrt()
            result_pow = number ** 0.5         # Using exponentiation
            
            print(f"\nResults:")
            print(f"Using math.sqrt(): {result_math}")
            print(f"Using pow: {result_pow}")
            
            # Demonstrate some other useful math functions
            print(f"\nOther mathematical calculations for {number}:")
            print(f"Ceiling: {math.ceil(result_math)}")
            print(f"Floor: {math.floor(result_math)}")
            print(f"Sin: {math.sin(number)}")
            print(f"Cos: {math.cos(number)}")
            
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator
calculate_root()

# Demonstrate some other useful built-in library functions
print("\nSystem Information:")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"Platform: {sys.platform}")

# Some useful mathematical constants from math library
print("\nMathematical Constants:")
print(f"π (pi): {math.pi}")
print(f"e: {math.e}")
print(f"τ (tau): {math.tau}")  # tau is 2π