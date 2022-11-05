'''
Define a class Student to store his/her name and marks in three subjects.
Use a class variable to store the maximum average marks of the class.Use
constructor and destructor to initialize and destroy the objects.
'''


class Student:
    avgScores = []
    def __init__(self, n,marks=[0,0,0]):
        self.name = n
        self.marks=marks
        self.calcAvg()

    def calcAvg(self):
        Student.avgScores.append((self.name, sum(self.marks)/len(self.marks)))
        print(Student.avgScores)
        return (sum(self.marks)/len(self.marks))

    def maxAvgMarks():
        maxAvg=0
        name=""
        for i in Student.avgScores:
              if i[1]>maxAvg:
                maxAvg=i[1]
                name=i[0]
        return (maxAvg,name)


students = [Student("Raj", [23, 34, 32]), Student("Qwe", [45, 34, 32]), Student("Ary", [23, 100, 32])]
print("Name of the student with highest average marks :",Student.maxAvgMarks()[1])
print("The student's average marks :",Student.maxAvgMarks()[0])

