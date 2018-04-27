import nltk
import json
# from ResultwithNameGender3 import Document
import model

f = open('ResultwithNameGender.json')
Document = json.load(f)
TEST_DOCUMENT = []
data = []
processed = 0
skipped = 0
unknownGender = 0

if __name__ == '__main__':
    for doc in Document:
        tokenString = doc['text']
        if len(tokenString) > 50:
            processed += 1
            if doc['gender'] == 'unknown':
                unknownGender += 1
            sentences = nltk.sent_tokenize(tokenString)
            prob = model.score({'text': tokenString, 'sentences': sentences})
            data.append({'text': tokenString, 'name': doc['name'],
                         'gender': doc['gender'], 'sentences': sentences,
                         'polite': "%3f" % prob['polite'],
                         'impolite': "%3f" % prob['impolite']})
        else:
            skipped += 1
    with open('ResultWith_NameGenderSentencesPoliteImpolite.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print("processed = ", processed)
    print("skipped = ", skipped)
    print("unknown gender = ", unknownGender)
