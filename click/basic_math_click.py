import click
@click.command()
@click.argument('numbera', type=int)
@click.argument('numberb', type=int)
@click.option('--operation', '-o', type=click.Choice(["add", "subtract", "multiply", "divide"]), required=True)
def cal(numbera, numberb, operation):
    if operation == "add":
        print(f"two number {operation} = {numbera+numberb}")
    elif operation ==  "subtract":
        print(f"two number {operation} = {numbera-numberb}")
    elif operation ==  "multiply":
        print(f"two number {operation} = {numbera*numberb}")
    elif operation ==  "divide":
        print(f"two number {operation} = {numbera/numberb}")
    else:
        print("Wrong operation")
        
if __name__ == '__main__':
    cal()