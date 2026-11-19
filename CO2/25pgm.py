def count Char(inputString)
Count={}
for char in inputString:
    if char in Count:
        Count[char]+=1
        else:
            Count[char]=1
return Count
str 2=input(Enter a string:")
result=countChar(str 2)
print(result)
