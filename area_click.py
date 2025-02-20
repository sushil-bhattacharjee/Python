import click
import math

@click.command()
@click.option('--shape', type=click.Choice(['circle', 'rectangle', 'triangle'], case_sensitive=False), 
              required=True, help='Input the shape type to calculate the area.')
@click.option('--radius', type=float, help='Input the radius of the circle.')
@click.option('--width', type=float, help='Input the width of the rectangle.')
@click.option('--height', type=float, help='Input the height of the rectangle or triangl.')
@click.option('--base', type=float, help='Input the base of the triangle.')

def area(shape, radius, width, height, base):
    """Calculate the area of a shape."""
    if shape == 'circle':
        result = math.pi * (radius ** 2)
        click.echo(f'The area of the circle with radius {radius} is {result:.2f}')
    elif shape == 'rectangle':
        result = width * height
        click.echo(f'The area of the rectangle with width {width} and height {height} is {result:.2f}')
    elif shape == 'triangle':
        result = 0.5 * base * height
        click.echo(f'The area of the triangle with base {base} and height {height} is {result:.2f}')
        
if __name__ == '__main__':
    area()
