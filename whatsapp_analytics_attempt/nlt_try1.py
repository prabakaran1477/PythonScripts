from nltk.tokenize import sent_tokenize, word_tokenize

# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# print(sent_tokenize(EXAMPLE_TEXT))
# print(word_tokenize(EXAMPLE_TEXT))

# from nltk.corpus import stopwords
# print set(stopwords.words('english'))

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))
raw_input(stop_words)

word_tokens = word_tokenize(example_sent)
raw_input(word_tokens)

filtered_sentence = [w for w in word_tokens if not w in stop_words]
raw_input(filtered_sentence)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
raw_input(word_tokens)
print(filtered_sentence)
raw_input(filtered_sentence)
