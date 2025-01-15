def analyze_file(filename):
    try:
        # Initialize counters
        line_count = 0
        word_count = 0
        
        # Open and read the file
        with open(filename, 'r') as file:
            for line in file:
                # Count lines (including empty ones)
                line_count += 1
                
                # Count words in this line
                # split() breaks the line into words using whitespace
                words = line.strip().split()
                word_count += len(words)
        
        # Print results
        print(f"Analysis of {filename}:")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Average words per line: {word_count/line_count:.2f}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# analyze_file('your_file.txt')