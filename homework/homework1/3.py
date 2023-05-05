text = input()
vowels = "aeiouAEIOU"
for vowel in vowels:
    text = text.replace(" ","")
    text = text.replace(vowel, ".")
print(text.swapcase())


