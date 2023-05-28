import gensim
import json
import random

google_news_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=200000)
def load_taboos():
    with open('./data/en/animals.json', 'r') as animal_file:
        # Exclude taboos that have space in it.
        return json.load(animal_file)

def get_taboo(key = None):
    data = load_taboos()
    filtered_data = dict()
    for key in data.keys():
        if ' ' not in key:
            filtered_data[key] = data[key]
    random_index = random.randint(0, len(filtered_data) - 1)
    random_animal = list(filtered_data)[random_index]
    return (random_animal, data[random_animal])

def is_valid(taboos: list[str], clue: str) -> bool:
    taboos = [str.lower(s) for s in taboos]
    for taboo in taboos:
        if clue in taboo or taboo in clue or '_' in clue:
            return False
    return True

(keyword, other_taboos) = get_taboo()
keyword = str.lower(keyword)
print(f"Keyword is '{keyword}' and other taboos are {other_taboos}.")
taboos = other_taboos + [keyword]

def print_similarities(model, keyword, taboos):
    counter = 1
    for (clue, simularity) in model.most_similar(keyword, topn=15):
        clue = str.lower(clue)
        if is_valid(taboos, clue):
            if counter == 1:
                print("Top matches:")
            print(f"{counter}.\t{simularity:.2f}\t{clue}")
            counter += 1

print_similarities(google_news_model, keyword, taboos)