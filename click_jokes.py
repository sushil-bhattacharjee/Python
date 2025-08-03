import click
import requests

@click.group()
def jokes():
    """CLI tool for fetching jokes from JokeAPI."""
    pass

@jokes.command()
@click.option('--category', default='Programming', type=click.Choice(['Programming', 
            'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas']), help='Category of joke')
@click.option('--lang', default='en', help='Language code (default: en)')
@click.option('--amount', default=1, type=int)
def getjoke(category, lang, amount):
    """Fetch a random joke."""
    url = f"https://v2.jokeapi.dev/joke/{category}?lang={lang}&format=json"
    if amount:
        url = f"https://v2.jokeapi.dev/joke/{category}?amount={amount}"
    else :
        url = f"https://v2.jokeapi.dev/joke/{category}?lang={lang}&format=json"
    resp = requests.get(url)
    # print(resp)
    data = resp.json()
    # print(data)

    if data.get("type") == "single":
        click.echo(data["joke"])
    elif data.get("type") == "twopart":
        click.echo(f"{data['setup']} ... {data['delivery']}")
    elif amount:
        for joke in data["jokes"]:
            if joke.get("type") == "single":
                click.echo(joke["joke"])
            elif joke.get("type") == "twopart":
                click.echo(f"{joke['setup']} ... {joke['delivery']}")        
    else:
        click.echo("No joke found or something went wrong.")

if __name__ == "__main__":
    jokes()
