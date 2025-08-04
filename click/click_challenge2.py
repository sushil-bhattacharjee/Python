# Challenge 2: Multiple Options with Different Types
# Create a Click command called create_file that:

# Takes a required argument filename
# Takes a --content option (string, default: "Hello World")
# Takes a --lines option (integer, default: 1) - repeats the content this many times
# Takes a --uppercase flag (boolean) - if present, converts content to uppercase
# Actually creates the file with the specified content

# Your code should work like this:
# bashpython script.py create_file test.txt
# # Creates test.txt with "Hello World"

# python script.py create_file test.txt --content "Python rocks" --lines 3 --uppercase
# # Creates test.txt with:
# # PYTHON ROCKS
# # PYTHON ROCKS  
# # PYTHON ROCKS
# Hints:

# Boolean flags in Click don't need type=bool - just use is_flag=True
# You can use content.upper() to convert to uppercase
# Use Python's built-in open() function to write the file

# Give it a shot!


import click


@click.command()
@click.argument('filename')
@click.option('--content', default="Hello, World!", help='Content to write to the file.')
@click.option('--lines', default=1, type=int)
@click.option('--uppercase', is_flag=True)
def create_file(filename, content, lines, uppercase):
    """A simple command line tool that takes a file and an option."""
    if uppercase:
        content = content.upper()
    with open(filename, 'w') as f:
        for i in range(0, lines):
            f.write(content+'\n')
            print(content)
    print(f"File '{filename}' created with content: {content}")
if __name__ == '__main__':
    create_file()