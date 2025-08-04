# Challenge 3: Command Groups
# Create a CLI tool with multiple commands using @click.group():

# Main group called filetools
# Command create (similar to what you just built)
# Command read that takes a filename and prints its contents
# Command count that takes a filename and counts lines/words/characters

# The usage should be:
# bashpython script.py create test.txt --content "Hello"
# python script.py read test.txt
# python script.py count test.txt

import click

@click.group()
def filetools():
    """A group of file-related commands."""
    pass
@filetools.command("create")
@click.argument('filename')
@click.option('--content', default="Hello World")
def create(filename, content):
    with open(filename, 'w') as f:
        f.write(content+'\n')
        
@filetools.command('read')
@click.argument('filename')
def read(filename):
    try:
        with open(filename, 'r') as f:
            result= f.read()
            click.echo(result)
    except FileNotFoundError:
        click.echo(f"File '{filename}' not found")

@filetools.command('count')
@click.argument('filename')
def count(filename):
    try: 
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            characters = len(content)
            click.echo(f"Line count: {len(lines)}")
            click.echo(f"Words count: {len(words)}")
            click.echo(f"Characters: {characters}")
    except FileNotFoundError:
        click.echo(f"File '{filename}' not found")

if __name__ == '__main__':
    filetools()