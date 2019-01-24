import string

# Constraints
# Capital and lower case versions of the same word should be counted is the same word.
# Remove punctuations from all words.
# Time: O(N)
# Space: O(N)

def word_count(sentence):
    if sentence == "":
        return {}
    else:
        c = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split(" ")
        wc = {x: c.count(x) for x in set(c)}
        return wc
 
 def uniq_words(sentence):
    if sentence == "":
        return {}
    else:
        c = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split(" ")
        uw = len(set(c))
        return uw

sntc = "I would not worry too much about the performance difference between the two approaches as it is marginal. I would really only optimise this if it proved to be the bottleneck in your application which is unlikely."
print(uniq_words(sntc))
