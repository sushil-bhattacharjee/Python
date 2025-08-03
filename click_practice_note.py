import click


@click.group()
def test():
    pass

@test.command()
@click.argument('filename')
@click.option('--content')
def write(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        
@test.command()
@click.argument('filename')
def read(filename):
    with open(filename, 'r') as f:
        result = f.read()
        click.echo(result)
        
if __name__ == '__main__':
    test()