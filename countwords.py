intro = input("enter your introduction:")
charactercount = 0
wordcount = 1
for i in intro:
    charactercount+=1
    if(i == " "):
        wordcount+=1
print(wordcount, charactercount)