import click
import requests

@click.group()
def car():
    pass


@click.command()
@click.argument('searchstring')
def searchbrands(searchstring):
    query = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json")
    car_brands = query.json()
    for carband in car_brands["Results"]:
        if searchstring.lower() in carband["Make_Name"].lower():
            print(carband["Make_Name"])
            
@click.command()
@click.argument('modelname')
@click.option('--year', type=int)
def listmodels(modelname, year):
    if year:
        query = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/{modelname}/modelyear/{year}?format=json")
    else:
        query = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{modelname}?format=json")
    output = query.json()
    for mod_name in output["Results"]:
        print(mod_name["Model_Name"])
            
car.add_command(searchbrands, name="search")
car.add_command(listmodels)
            
if __name__ == '__main__':
    car()