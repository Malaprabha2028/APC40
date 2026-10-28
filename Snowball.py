from nltk.stem import SnowballStemmer

ss = SnowballStemmer("english")

print(ss.stem("playing"))
print(ss.stem("played"))
print(ss.stem("plays"))