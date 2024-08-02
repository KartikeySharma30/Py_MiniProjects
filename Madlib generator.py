
# Its is a Project Which help to read a text from a file and from it allow you to build the storyline your way by putting in
# Different Different words according to the Grammatical positions in that text and Design it your way.


with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/mini Proj/story.txt","r") as st:
    sto=st.read()
words =set()
start_of_word =-1
# Here we are Finding those grammatical Position to Add words 
target_strt = "<"
target_end = ">"

for i,char in enumerate(sto):
    if(char == target_strt):
        start_of_word=i
    if char == target_end and start_of_word!=-1:
        word = sto[start_of_word:i+1]
        words.add(word)
        start_of_word = -1
anss={}

# Here we are Assigning Words to Those Positons in the Text which we recieved 
for word in words:
        ans=input(f"Enter a word for {word}:")
        anss[word]=ans
#print(words)
for word in words:
    sto=sto.replace(word,anss[word])
    
print(sto)

