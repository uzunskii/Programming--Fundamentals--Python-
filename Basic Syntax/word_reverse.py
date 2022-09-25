word = input()
reverse = ""
symbols = len(word)
for count in range(symbols -1, -1, -1):
    reverse += word[count]
print(reverse)
