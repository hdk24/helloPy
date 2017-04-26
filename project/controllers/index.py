from flask import jsonify, request
from project import app
from project.models.languages import Languages

# define data
languages = Languages().get_languages()
entity_message = 'message'


# get index endpoint
@app.route("/", methods=['GET'])
def hello():
    return jsonify({entity_message: 'Hello world!', 'url': 'http://prettyprinted.com/'})


# get all language endpoint
@app.route("/lang", methods=['GET'])
def return_lang():
    return jsonify({entity_message: languages})


# get based id /lang/[id]
@app.route('/lang/<int:id>', methods=['GET'])
def return_one(id):
    indexs = [ids for ids in languages if ids['id'] == id]  # return array
    return jsonify({entity_message: indexs})


# add data param -> name
@app.route('/lang', methods=['POST'])
def add_one():
    id_new = len(languages) + 1
    params_name = request.form['name']
    language = {'id': id_new, 'name': params_name}
    languages.append(language)
    return jsonify({entity_message: languages})



