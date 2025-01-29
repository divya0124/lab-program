import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")
def extract_pos(sentence):
    doc = nlp(sentence)
    nouns = [ ]
    verbs = [ ]
    adjectives = [ ]
    for token in doc:
        if token.pos_ == "NOUN":
            nouns.append(token.text)
        elif token.pos_ == "VERB":
            verbs.append(token.text)
        elif token.pos_ == "ADJ":
            adjectives.append(token.text)
    return nouns, verbs, adjectives 
sen = pd.read_csv ('textclassification.csv')
n = [] 
v = []
a = []
for sentence in sen['sentence']:
    noun, verb, adjective=extract_pos(sentence)
    n.extend(noun)
    v.extend(verb)
    a.extend(adjective)
print("\n\t\t\t NOUNS , VERBS , ADJECTIVES")
print("\t\t\t ------------------------------")
print("Nouns:", n)
print("Verbs:", v)
print("Adjectives:", a)  
 
