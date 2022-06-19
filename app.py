from flask import Flask, jsonify, request, render_template, redirect
from jinja2 import Template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('homepage.html')

@app.route("/usercards")
def show_card_table():
    return render_template('pokemon cards.html')

@app.route("/usertrainers")
def show_trainer_table():
    return render_template('trainer cards.html')

@app.route("/sourcecode")
def github():
    return redirect("https://github.com/jrtcra")

@app.route("/resources")
def show_resource():
    return redirect("https://www.pokellector.com/")

pokemon_cards = [{'name': 'Glaceon', 'type': 'Water', 'stage': 'V', 'hp': '210', 'rarity': 'Ultra Rare'},
        {'name': 'Rayquaza', 'type' : 'Dragon', 'stage': 'VMAX', 'hp': '320', 'rarity': 'Holo Rare VMAX'},
        {'name': 'Celebi', 'type': 'Grass', 'stage': 'VMAX', 'hp': '310', 'rarity': 'Holo Rare VMAX'},
        {'name': 'Lycanroc', 'type': 'Fighting', 'stage': 'VMAX', 'hp': '320', 'rarity': 'Holo Rare VMAX'}]

trainer_cards = [{'name': 'Doctor', 'rarity': 'Full Art'},
        {'name': 'Nessa', 'rarity': 'Full Art'},
        {'name': 'Honey', 'rarity': 'Full Art'},
        {'name': 'Peonia', 'rarity': 'Full Art'},
        {'name': 'Chili & Cilian & Cress', 'rarity': 'Rainbow Rare'},
        {'name': 'Copycat', 'rarity': 'Full Art'}]

@app.route('/trainer', methods=['GET'])
def get_all_trainers():
    return jsonify({'list': trainer_cards})

@app.route('/cards', methods=['GET'])
def get_all_cards():
    return jsonify({'list': pokemon_cards})

@app.route('/cards/<string:name>', methods=['GET'])
def get_one_card(name):

    return_type = pokemon_cards[0]
    for get_type, get_pokemon in enumerate(pokemon_cards):
        if get_pokemon['name'] == name:
            return_type = pokemon_cards[get_type]
            return return_type 
        elif get_pokemon['name'] != name:
            return_type = "entry does not exist"
    return jsonify({'This Pokemon type is ' : return_type})

@app.route('/cards', methods=['POST'])
def add_card():
 
    new_pokemon_card = request.get_json()
    pokemon_cards.append(new_pokemon_card)
    return jsonify({'new pokemon card': new_pokemon_card})

@app.route('/cards/<string:name>', methods=['PUT'])
def edit_card(name):
    update = request.get_json()
    for get_type, get_pokemon in enumerate(pokemon_cards):
        if get_pokemon['name'] == name:
            pokemon_cards[get_type] = update
    us = request.get_json()
    return jsonify({"list all cards": pokemon_cards})

@app.route('/cards/<string:name>', methods=['DELETE'])
def delete_card(name):
    return_type = pokemon_cards[0]
    for get_type, get_pokemon in enumerate(pokemon_cards):
        if get_pokemon['name'] == name:
            del pokemon_cards[get_type]
    return jsonify({'Here is our database now ': pokemon_cards})

if __name__ == '__main__':
    app.run(debug=True)

