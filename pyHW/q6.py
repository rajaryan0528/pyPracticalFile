'''
Define a class Product that stores information about products manufactured by a company. The class should contain the following data members:  
• name–Name of the Product 
• material– Material with which Product is made of ‘Metal’ or ‘Plastic’. 
• costPrice– Cost of the Product in rupees. Include assert statement to ensure that the cost 
is between 25 and 250.  
• discount–  Deduction  in  cost  of  the  Product.  It  is  equal  to  20%  of  costPrice  if  the material is ‘Metal’ and 10% for ‘Plastic’. 
• count - number of objects created for Product class. Add appropriate statements in the code 
to increment the value of count by 1, when an object is created. Use assert statement to check 
that count is always greater than equal to 0. 
 
The class should support the following methods: 
• _init_() for initializing data members.  
• sellingPrice() which computes and displays selling price where selling price is calculated as difference of costPrice and discount  
• display() which displays the information about the product. 
 
Also write Python statements for the following:  
 
• Create  a  product  ‘Plate’  of  ‘Metal’  having  costPrice  as  170.  Display  the  value  of count.  
• Create a product ‘Spoon’ of ‘Plastic’ having costPrice as 26. Display the value of count.  
• Compute  and  display  the  selling  price  of  ‘Plate’  and  ‘Spoon’.
'''


class product:
    count = 0

    def __init__(self, n, m, cp):        #constructor 
        product.count += 1
        self.name = n
        self.material = m
        assert 25 <= cp <= 250, "the cost price must be between 25 and 250."
        self.costPrice = cp
        if (self.material == "metal"):     #sets the value of discount accordingly
            self.discount = 0.2*self.costPrice
        else:
            self.discount = 0.1*self.costPrice
        assert product.count > 0

    def sellingPrice(self):
        return self.costPrice-self.discount

    def display(self):
        print("Name of the Product: ", self.name)
        print("Material with which Product is made of : ", self.material)
        print("Cost of the Product(in rupees): ", self.costPrice)
        print("Discount of : ", self.discount)
        print(product.count)


ob1 = product("Plate", "Metal", 170)
ob1.display()
ob2 = product("Spoon", "Plastic", 26)
ob2.display()
print("Selling Price of %s(in rupees): " % (ob1.name), ob1.sellingPrice())
print("Selling Price of %s(in rupees): " % (ob2.name), ob2.sellingPrice())
