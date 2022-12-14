'''
Write a function that takes a sentence as input from the user
and calculates the frequency of each letter.Use a variable of dictionary type to
maintain the count
'''
import json
def freqOfLetters(s):
    count={}    #letter:count
    for letter in s :
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1
    return count
def main():
 sentence=input("Enter a sentence :")
 print(json.dumps(freqOfLetters(sentence),indent=4))

if __name__=="__main__":
    main()