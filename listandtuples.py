def sumAvg(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    return total_sum, average

if __name__ == "__main__":
    try:
        numbers = input("Enter numbers separated by comma: ").split(",")
        numbers = [int(num) for num in numbers]  
        total_sum, average = sumAvg(numbers)
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")
    except ValueError:
        print("Please enter valid numbers separated by commas.")