from nltk.stem import PorterStemmer

ps = PorterStemmer()

print(ps.stem("playing"))
print(ps.stem("played"))
print(ps.stem("plays"))