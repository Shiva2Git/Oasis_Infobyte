def string(strs):
  a=[i for i in strs]
  vowels=['a','A','e', 'E', 'i', 'I','o', 'O', 'u', 'U']
  for i in range(len(a)):
    for j in vowels:
       if strs[i]==j:
         a.remove(strs[i])
  return ''.join(a)

s=input('enter a string :'.upper())
print(string(s))