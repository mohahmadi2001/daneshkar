mystr = 'www.google.com'
mydic={}
for char in mystr:
   #  if char in mydic:
   #     mydic[char] += 1
   #  else:
   #     mydic[char] = 1
   mydic[char]=mydic.get(char,0)+1
print(mydic)


