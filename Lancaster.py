from nltk.stem import LancasterStemmer

ls = LancasterStemmer()

print(ls.stem("playing"))
print(ls.stem("played"))
print(ls.stem("plays"))