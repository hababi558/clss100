userInput = input('Your introduction: ')

print(userInput)

characterCount = 0
wordCount = 1

for Count in userInput:
    characterCount=characterCount+1
    

    if(Count==' '):
        wordCount=wordCount+1
print('Number Of Character')
print(characterCount)
print('Number of words') 
print(wordCount)