# created by Gourav as on 5-1-2021
#Sum of tow numbers Class 
class Sumofnum:
    #constractor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    # Normal Function 
    def summ(self):
        return self.num1+self.num2
    
    # Function overloding
    def summ(self,num1,num2):
         return num1+num2
    # Multi number sum 
    def multisum(self,*num):
        return sum(num) 

# creating objaect
obj1 = Sumofnum(2,8)
print(f"First number:{obj1.num1}")
print(f"Second number:{obj1.num2}")
#print(obj1.sum1())
print(f"Sum of {obj1.num1} + {obj1.num2} : {obj1.summ(14,6)}")
print("Sum of Multi Number Sum:",obj1.multisum(9,1,2,9))