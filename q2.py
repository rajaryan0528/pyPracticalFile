'''
Consider a showroom of electronic products,where there are various salesmen.Each salesman is given a commission of 5%,depending
on the sales made per month.In case the sale done is less than 50000,then the salesman is not given any commission.
Write a function to calculate total sales of a salesman in a month,commission and remarks for the salesman.
Sales done by each salesman per week is to be provided as input.Use tuples/list to store data of salesmen.Assign remarks according to the
following criteria:
Excellent:Sales>=80000
Good:Sales>=60000and<80000
Average:Sales>=40000and<60000
WorkHard:Sales<40000
'''

def saleCalc(l):
    monthlySales=0
    commision=0
    remark=""
    data=()      #commision,remark
    for i in l:
        monthlySales+=i
    print("Monthly Sales :",monthlySales)
    if(monthlySales<40000):
        commision=0
        remark="Work Hard"
        data=commision,remark
    elif(40000<monthlySales<60000):
         if(monthlySales<50000):
            commision=0
            remark="Average Sales"
         else:
               commision=0.05*monthlySales
               remark="Average Sales"
         data=commision,remark

    elif(60000<=monthlySales<80000):
        commision=0.05*monthlySales
        remark="Good"
        data=commision,remark

    else:
       commision=0.05*monthlySales
       remark="Excellent"
       data=commision,remark

    return data



print("Enter the sales per week as a list.")
sales=eval(input())
data=saleCalc(sales)
print("Commission Amount :",data[0])
print("Remark :",data[1])
