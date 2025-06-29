with open("story.txt","r",encoding="utf-8") as f:
    story = f.read()

start_of_words = -1
target_start = "<"
target_end = ">"

words = set()
for i,char in enumerate(story):
    if char == target_start:
        start_of_words = i
    
    elif char == target_end and start_of_words != -1:
        word = story[start_of_words:i+1]
        words.add(word)

myDictionary = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    myDictionary[word] = answer

for word in words:
    story= story.replace(word,myDictionary[word])
print(story)