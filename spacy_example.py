import spacy

# Extract named entities (like people, companies, amounts) from text
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")