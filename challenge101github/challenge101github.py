import click
import requests
import json

class GitHubRestApi:
    headers = {}

    def __init__(self, token):
        self.headers["Authorization"] = f"token {token}"
        self.headers["Accept"] = "application/vnd.github.v3+json"

    def get(self, endpoint, params=None):
        url = f"https://api.github.com{endpoint}"
        resp = requests.get(url, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.json()

    def patch(self, endpoint, body):
        url = f"https://api.github.com{endpoint}"
        resp = requests.patch(url, headers=self.headers, data=json.dumps(body))
        resp.raise_for_status()
        return resp.json()

## Requirement B
@click.group()
@click.pass_context
##
def challenge101(ctx):
    ctx.ensure_object(dict)
    config = json.load(open("config.json"))
    ctx.obj["github"] = GitHubRestApi(config["GITHUB_PAT"])


## Requirement C
@challenge101.command()
@click.pass_obj
@click.option('--visibility')
##
def listrepos(obj, visibility):
    repos = obj["github"].get("/user/repos", params={"visibility": visibility})
    print("Repositories:")

    ## Requirement D
    # result = repos.json()
    for name in repos:
        print(name["name"])

    ##

## Requirement E
@challenge101.command()
@click.pass_obj
@click.option('--repo')
##
def listissues(obj, repo):
    print("Issues in repository:")
    ## Requirement F
    issues = obj["github"].get(f"/repos/sushil-bhattacharjee/{repo}/issues")
    for i in issues:
        print(f"- #{i['number']} {i['title']} (state: {i['state']})")
    ##

## Requirement G
@challenge101.command()
@click.pass_obj
@click.option('--repo')
@click.option('--issue')
@click.option('--state')
##
def setstatus(obj, repo, issue, state):
    body = {
        "state": state
    }
    response = obj["github"].patch(f"/repos/sushil-bhattacharjee/{repo}/issues/{issue}", body=body)
    print(f"Issue #{response['number']} is now {response['state']}")


if __name__ == "__main__":
    challenge101()
