s = input("Enter message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch.isalpha():
        result += chr((ord(ch.lower()) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted message:", result)

# Decryption
decrypt = ""

for ch in result:
    if ch.isalpha():
        decrypt += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypt += ch

print("Decrypted message:", decrypt)