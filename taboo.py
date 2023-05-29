import json
import random
import gensim
import gensim.downloader as api

# Binary is faster.
# Download from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
google_news_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=200000)
# google_news_model = api.load('word2vec-google-news-300')
twitter_model = api.load('glove-twitter-25')
wiki_model = api.load('glove-wiki-gigaword-50')

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

def get_similarities(model, keyword, taboos):
    results = []
    for (clue, simularity) in model.most_similar(keyword, topn=8):
        clue = str.lower(clue)
        if is_valid(taboos, clue):
            results.append((clue, simularity))
    return results

def print_results(results):
    for (clue, similarity) in results:
        print(f"{similarity:.2f}\t{clue}")


print("Matches for google news")
print("---")
print_results(get_similarities(google_news_model, keyword, taboos))
print("\nMatches for glove twitter")
print("---")
print_results(get_similarities(twitter_model, keyword, taboos))
print("\nMatches for glove wiki")
print("---")
print_results(get_similarities(wiki_model, keyword, taboos))
