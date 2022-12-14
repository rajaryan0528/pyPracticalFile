'''
Use dictionary to store marks of the students in 4 subjects.
Write a function to find the name of the student securing the highest percentage.
(Hint:Names of students are unique).
'''

def percentage(l):
    sum=0
    for i in range(4):
        sum+=l[i]
    return sum/4

def nameOfStu(data):
    temp = ()
    percentData = ()  # nested tuple
    for student in data:
       temp=(student,percentage(data[student]))     #([marks],percent)
       percentData+=temp,
    del temp

    max=0
    s=""
    for i in range(4):
       if percentData[i][1]>max:
        max=percentData[i][1]
        s=percentData[i][0]   #marks of student whose percentage is the highest

    return s


def main():
    data = {}
    for i in range(0, 4):
        key = input("Enter student's name : ")
        l = eval(input("Student's marks in 4 subjects as a list :"))
        data[key] = l
    print("Entered data : ")
    print(data)
    print("Student with highest marks :",nameOfStu(data))

if __name__=="__main__":
    main()