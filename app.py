import requests
import sqlite3 as sql
import urllib
from random import randint
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

FILENAME = "../../Downloads/Cloud-master/ZKHP.html"
con = sql.connect(FILENAME)
C = con.cursor()

# ID set is used to make sure the recipes have a unique ID
# APP_ID and API_KEY were given by Edamame to create an account to use the API

IDS = {-1}
APP_ID = '8228a6c6'
API_KEY = 'bd00528170e470eae3f228cb5bc7a1fc'
URL = f'https://api.edamam.com/search?/app_id=8228a6c6&app_key=bd00528170e470eae3f228cb5bc7a1fc'




# The following code is for the Recipe APP

@app.route('/')
@app.route('/home')
def home():
    return render_template("ZKHP.html")

# The following lines are for searching recipes from the API

@app.route('/submit', methods=['GET', 'POST'])
def result():
    output = request.form.to_dict()
    print(output)
    Ingredient = output["Ingredient"]

def main():
    #This program allows the user to search for recipes online using the API.

    print()
    command = ''
    while command.lower() != 'q':
        print("1) Find New Recipe")
        print("2) Search Saved Recipes")
        command = input("\t>> ")
        print()
        if command == '1':
            query_recipes()
        elif command == '2':
            search_my_recipes()
    C.close()



@app.route('/ZKHP.html', methods=['GET','POST'])
def query_recipes():
   
# Search and select recipe to view from API.
 
    response = None
    success = False
    index = 0
    while not success:
        print("Please enter a keyword")
        key_word = input("Please enter a keyword: ")
        print(key_word)
        data = make_request(get_url_q(key_word))
        data = data['hits']
        if len(data) > 0:
            success = True
        else:
            print(f'0 results for "{key_word}"')
            input("")
    index = display_recipe_labels(data, index)
    print(f"   Select Recipe # (1-{index})\n   (enter 'm' to see more)")
    select = select_from_index(index)
    # Enables user to query 20 more recipes with same keyword
    if select == 'm' and index == 20:
        _from = 20
        to = 40
        data2 = make_request(get_url_q(key_word, _from, to))
        data2 = data2['hits']
        index = display_recipe_labels(data2, index)
        # join the data of both requests together
        data += data2
        # selection has not yet been made
        select = -1
    select_recipe(data, index, select)



def display_recipe_labels(data, index):
   # Shows all recipes from the result of the request.
    
    print()
    for recipe in data:
        index += 1
        print(f"   {index})", recipe['recipe']['label'])
    print()
    return index

