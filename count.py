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
   
def avg_word_length(sentence):
    words = sentence.split()
    retturn sum(map(len, words))/len(words)

sentence = "Hi my name is Bob"
print(avg_word_length(sentence))

def uniq_words(sentence):
    if sentence == "":
        return {}
    else:
        c = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split(" ")
        uw = len(set(c))
        return uw

sntc = "I would not worry too much about the performance difference between the two approaches as it is marginal. I would really only optimise this if it proved to be the bottleneck in your application which is unlikely."
print(uniq_words(sntc))

### 10. Count the number of times a substring appear in a string

def count_combinations(s, subs):
    subl = len(subs)
    e = len(s) - subl + 1
    comb = 0
    for i in range(0, e):
        if s[i:i+subl] == subs:
            comb+=1
    return comb

print(count_combinations("dddddd", "ddd"))

# simplest one, but does not count all combinations
print("dddddd".count("ddd"))
