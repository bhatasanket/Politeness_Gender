import json
from pprint import pprint
import features.vectorizer as strategyAPI
import csv

data = []
newdata = []
strategies = []

with open('ResultAfterParse.json') as data_file:
    data = json.load(data_file)

vectorizer = strategyAPI.PolitenessFeatureVectorizer()
# data = data[0]
for part in data:
    f = vectorizer.features(part)
    # Print summary of features that are present
    # print "\n===================="
    # print "Text: ", part['text']
    # print "\tUnigrams, Bigrams: %d" % len(
    #     filter(lambda x: f[x] > 0 and ("UNIGRAM_" in x or "BIGRAM_" in x), f.iterkeys()))
    # print "\tPoliteness Strategies: \n\t\t%s" % "\n\t\t".join(
    #     filter(lambda x: f[x] > 0 and "feature_politeness_" in x, f.iterkeys()))
    # print "\n"
    part["Unigrams, Bigrams"] = "%d" % len(
        filter(lambda x: f[x] > 0 and ("UNIGRAM_" in x or "BIGRAM_" in x), f.iterkeys()))
    part.pop('unigrams', None)
    q = []
    q.append(filter(lambda x: f[x] > 0 and "feature_politeness_" in x, f.iterkeys()))
    part["Politeness Strategies"] = q
    # part["Politeness Strategies"] = "%s" % "".join(
    #     filter(lambda x: f[x] > 0 and "feature_politeness_" in x, f.iterkeys()))
    newdata.append(part)

with open('FinalResult.json', 'w') as outfile:
    json.dump(newdata, outfile, indent=4)
    print("Completed")
