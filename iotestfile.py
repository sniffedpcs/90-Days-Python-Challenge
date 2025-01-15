# Create a sample file
def create_sample_file(filename):
    sample_text = """This is a test file.
It has multiple lines of text.
We will count these lines and words.

This is the final line."""

    with open(filename, 'w') as file:
        file.write(sample_text)
    
    print(f"Sample file '{filename}' created successfully!")

# Create and analyze the sample file
filename = 'sample.txt'
create_sample_file(filename)
#analyze_file(filename)