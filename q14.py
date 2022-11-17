'''Write a function that reads a file file1 and copies only alternative lines to
another file file2. Alternative lines copied should be the odd numbered lines.
UseException'''


def copyAlternativeLines(f1,f2):

    try:
     file1=open(f1,"r")
     file2=open(f2,"a+")
     lines=file1.readlines()
     print(lines)
     for line in range(0,len(lines)+1):
        if line%2==0:
            pass
        else:
            file2.write(lines[line])
        
    except EOFError:
        print("Reached the end of the file")
    except:
       print("Ran into some error :(")
    else:
        print("Successfully copied data of ", file1, " to ", file2)
        file1.close()
        file2.close()


file1="from.txt"
#file2=input("Enter the path of file where the data is to be copied :")
file2="to.txt"
copyAlternativeLines(file1,file2)
