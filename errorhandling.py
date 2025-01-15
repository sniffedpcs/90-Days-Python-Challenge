def get_valid_number():
    while True:
        try:
            # Get user input
            user_input = input("Please enter a number: ")
            
            # Try to convert it to an integer
            number = int(user_input)
            
            # Additional validation if needed
            if number < 0:
                raise ValueError("Please enter a positive number")
                
            print(f"You entered the valid number: {number}")
            return number
            
        except ValueError as e:
            # Check if this is our custom error message
            if str(e) == "Please enter a positive number":
                print(e)
            else:
                print("Error: Please enter a valid integer, not text or decimals.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            break
        finally:
            print("--- End of input attempt ---")

# Let's use the function in a simple calculator
def simple_calculator():
    try:
        print("Simple Calculator")
        number1 = get_valid_number()
        number2 = get_valid_number()
        
        # Demonstrate error handling with division
        try:
            result = number1 / number2
            print(f"Result of {number1} / {number2} = {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Calculator program finished")

# Run the calculator
simple_calculator()