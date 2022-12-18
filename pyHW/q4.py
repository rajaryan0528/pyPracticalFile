'''
Write  a  Python  code  snippet  to  read  a  text  file,  ‘file1.txt’,  line  by  line.  For  each  line  read  from ‘file1.txt’, split the text into words and count the number of characters and vowels in each word. Write each word along with its character count and vowel count separated by a question mark(?) in file ‘file2.txt’; with each word and its corresponding character count and vowel count in separate lines. Display the contents of ‘file2.txt’on the console.  
 
Handle the exception if ‘file1.txt’does not exist.  For example, the contents of ‘file1.txt’are as shown below. Python code snippet should create ‘file2.txt’ having contents as shown below:  
“file1.txt” 
Hello World 
Python is interesting 
 
“file2.txt” 
Hello?5?2 
World?5?1 
Python?6?1 
Is?2?1 
Interesting?11?4
'''


def count(word):  # counts the number of characters and vowels in the passed string
    vowels = 0
    chars = 0
    for i in range(len(word)):
        if word[i] in "aieou":
            vowels += 1
        if (word[i].isalpha()):
            chars += 1
    return (chars, vowels)


try:
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "w")
    lines = f1.readlines()  # list containg all the lines
    for i in lines:
        for j in i.split():  # iterating over words in each line
            f2.write(j+"?"+str(count(j)[0])+"?"+str(count(j)[1])+"\n")

except FileNotFoundError:
    print("File not found.")
    #  x- open a file only for exclusive creation. If the file already exists, this operation fails.
    fp = open('file1.txt', 'x')
    fp.close()
    print("Created the file file1.txt for you.")
except EOFError:
    print("Reached End of File.")
except Exception as err:
    print("Ran into some error.")
    print(type(err))
else:
    print("Operation Successful.Closing the file handles.")
    f1.close()
    f2.close()
