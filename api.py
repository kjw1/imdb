from flask import Flask, request
import json

app = Flask(__name__)

index = {}
movies = {}

def init():
    with open('items.json', encoding='utf-8') as f:
        raw_items = json.load(f)

    for raw_item in raw_items:
        movies[raw_item['title']] = raw_item
        for director in raw_item['directors']:
            add_to_search(director, raw_item['title'])
        for cast in raw_item['cast']:
            add_to_search(cast, raw_item['title'])

def add_to_search(full_term: str, title: str):
    terms = full_term.lower().split(" ")
    for term in terms:
        if term not in index:
            index[term] = set()
        index[term].add(title)

@app.route('/')
def hello():
    return json.dumps(movies, indent=4)

@app.route('/search', methods=['POST'])
def search():
    query = request.args.get('query', '')
    terms = query.split(" ")
    output_set = set()
    for term in terms:
        if term in index:
            found = index[term]
            if len(output_set) > 0:
                output_set = output_set.intersection(found)
            else:
                output_set = found.copy()
    
    return json.dumps(list(output_set))


init()