class perfume:
   def __init__(self, crown, neck,body,):
    self. crown= crown
    self.neck = neck
    self.body= body
      
  def isperfume(self):
   return True
class Creed_Aventus(perfume):

  def isCreed_Aventus(self):
    return True


Creed_Aventus = Creed_Aventus(1, 'gold', 'silver')
print(Creed_Aventus.crown) 
print(Creed_Aventus.neck)
print(Creed_Aventus.body)
print(Creed_Aventus.isperfume())
print(Creed_Aventus.isCreed_Aventus())


#ans:Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

class phone:
  def __init__(self, screen, battery,speaker,):
    self. screen= screen
    self. battery= battery
    self.speaker= speaker
  
  def isphone(self):
    return True
  

class Samsung(phone):

  def isSamsung(self):
    return True


Samsung = Samsung(1, 'black', 'green')
print(Samsung.screen) 
print(Samsung.battery)
print(Samsung.speaker)
print(Samsung.isphone())
print(Samsung.isSamsung())

# create a wallet
# add bitcoin to wallet
# spend from our wallet
bitcoin_wallet=input("Enter your full name?")
print("This is "+  bitcoin_wallet + "'s " + "wallet" )
my_bitcoin_wallet_balance=10
print(bitcoin_wallet, " balance is: ", my_bitcoin_wallet_balance)
print(bitcoin_wallet,"balance is 10 bitcoin")
#Get credit amount from the user
credit_amount=int(input("Enter your credit amount"))
#We are adding our credit amount to our bitcoin wallet balance
if credit_amount > 0:
  my_bitcoin_wallet_balance=credit_amount + my_bitcoin_wallet_balance
print("Your new balance is",my_bitcoin_wallet_balance,"bitcoin")
transaction_amount=int(input("Enter amount you would like to withdraw"))
spent_bitcoin_balance=my_bitcoin_wallet_balance - transaction_amount



#Display all the livestocks available on the farm together with the overall price of the
#product, e.g. for cattle, the total price would be the quantity multiplied by the
#price/unit, i.e. cattle_total_amount = quantity x price/unit = 58 x 5 = 290. This should
#be done for all the products and should be displayed on the console like this “The
#total price of cattle is”, cattle_total_amount




print("WELLCOME TO ISL LIVE STOCK FARM")


# Cattle
animal1 = 'Cattle'
animal1_amount = 340
animal1_quantity = 5
animal1_total_amount = animal1_amount * animal1_quantity

print("Animal", '\t\t', "Quantity" , '\t\t', "Amount", '\t\t', "total_amount")
print(animal1, '\t\t\t   ', animal1_quantity, '\t\t   ', animal1_amount, ' \t\t\t\t', animal1_total_amount)

#pig
animal2 = 'pig'
animal2_amount = 82
animal2_quantity = 2
animal2_total_amount = animal2_amount * animal2_quantity

print(animal2, '\t\t\t   ', animal2_quantity, '\t\t   ', animal2_amount, ' \t\t\t\t', animal2_total_amount)

#sheep
animal3 = 'sheep'
animal3_amount = 18
animal3_quantity = 3
animal3_total_amount = animal3_amount * animal3_quantity

print(animal3, '\t\t\t   ', animal3_quantity, '\t\t   ', animal3_amount, ' \t\t\t\t', animal3_total_amount)

#goats
animal4 = 'goats'
animal4_amount = 113
animal4_quantity = 1
animal4_total_amount = animal4_amount * animal4_quantity

print(animal4, '\t\t\t   ', animal4_quantity, '\t\t   ', animal4_amount, ' \t\t\t\t', animal4_total_amount)

#horse
animal5 = 'horse'
animal5_amount = 20
animal5_quantity = 10
animal5_total_amount = animal5_amount * animal5_quantity

print(animal5, '\t\t\t   ', animal5_quantity, '\t\t   ', animal5_amount, ' \t\t\t\t', animal5_total_amount)




# school_wallet=input(" What do you want to buy ?")
# print("you have successfully  brought a " +  school_wallet)


print("welcome to fizz buzz")
number=int(input("input number"))
if number //  3:
  print("fizz") 
elif number // 5:
  print("buzz")
elif number //5 and number //3:
  print("fizz_buzz")
else:
  print("try again")



print("Welcome to Fizzbuzz game")
i=int(input("Enter any number divisible by five,three or both: "))
if i % 5==0 and i % 3==0:
    print("Fizzbuzz")
elif i % 3==0:
    print("Fizz")
elif i % 5==0:
    print("Buzz")
else:
   print("Invalid number") 

"""
This class is to explain the concept of inheritance
- Inheritance is a pillar of Object Oriented Programming
- In inheritance we use the 'is-a' relationship
- Closeup is-a type of toothpaste
- A Dog is-a type of Animal
"""

class Animal:
  #Create a constructor
  def __init__(self, legs, eyes, furr):
    self.legs = legs
    self.eyes = eyes
    self.furr = furr
  
  def isAnimal(self):
    return True
  

class Dog(Animal):

  def isDog(self):
    return True


snuggle = Dog(6, 'green', 'brown')
print(snuggle.legs) #6
print(snuggle.eyes) #green
print(snuggle.furr) #brown
print(snuggle.isAnimal()) #True
print(snuggle.isDog()) #True

# What are some reasons we use inheritance in programming?
# Create an inheritance relationship between any Two entities (give them your own defined attributes and behaviors) 




class Math:
  def multiply(self, *args):
    multiply = 1
    for number in args: 
      multiply = multiply × number

    return multiply

  


math = Math()

answer = math.multiply(1, 2, 3)
print(answer)

# answer2 = math.sum(1, 2) 


print("WELLCOME TO ISL LIVE STOCK FARM")



Name{animal1='Cattle',animal1_amount=340,animal1_quantity=5,animal1_total_amount=animal1_amount*animal1_quantity}

print('Name')







class math:
  def multiply(self, *args):

    #[5,2,3,4,5]
     multiple = 1

    for num in args:
      multiple = multiple * num
  
     return multiple 




class Math:
  def sum(self, *victor):
    sum = 0
    for number in victor: 
      sum = sum + number

    return sum

  


math = Math()

answer = math.sum(1, 2, 3)
print(answer)

# answer2 = math.sum(1, 2) 



# create a function that finds the b power of a

# parameters - What is needed
# arguments - What is given

# function definition
def power(a, b):
  answer = a**b
  print(answer)

# function call
a = 3
b = 4
power(a, b)

# Create 4 fucntions
#  1. add two numbers
#  2. subtract number b from a
#  3. multiply a and b
#  4. prin
# What is mean?
# Mean is the mathematical avarage of a set of number

# What is the difference(s) between list/arrays and ellipsis

# numbers = [15, 23, 10, 45, 37]



def mean(*numbers):
  print('Ohh, I am happy to be here')
  print(numbers)
  # answer

mean(15, 23, 10, 45, 37)
# What is median?
# Median is the middle number amongst a group of number arranged in ascending or desc order.

# What is mode?
# Mode is the number that occur most often in a data set.


# how to calculate mean
# sum of all the numbers divided by the amount of the numbers

# how to calculate/find median
# arrange numbers in desc/asc order, then pick the number in the middle
# if there are two numbers in the middle, add the two numbers and find their average.

# calculate/find mode
# pick the most occuring number in the dataset.
# 


