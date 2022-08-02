var = "James" * 2  * 3
print(var)


# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)


salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)


for x in range(1, 10, 2):
  print(x)


for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )


# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)


def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)


var= "James Bond"
print(var[2::-1])

str = "pynative"
print (str[1:3])


p, q, r = 10, 20 ,30
print(p, q, r)

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]
print(listOne == listTwo)
print(listOne is listTwo)



# valueOne = 5 ** 2
# valueTwo = 5 ** 3
# print(valueOne)
# print(valueTwo)


for i in range(10, 15, 1):
  print( i, end=', ')
  


x = 36 / 4 * (3 +  2) * 4 + 2
print(x)


# Reverse a string
var = 'ajaythakur'
print(var[::-1])


#check palindrome
a = input('Enter word: ')
b = a[::-1]
if a == b:
    print('Palindrome')
else:
    print('Not palindrome')
