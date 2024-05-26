#return statement = a statement used within a function to send python value/object back to the caller!!**
#                    ***and these value/objects known as function's return value!****

def multiply(number1,number2):
    result = number1 * number2
    return result
x = multiply(6,7)
y = multiply(3.8,4)
print(x)
print(y)

def multiply(a,b):
    r = a * b

x = multiply(2,4)
print(x)

def multiply(number1,number2):
    result = number1*number2
    return result

x = multiply(6,7)
print(x)

def multiply(a,b): #way of writting code in less lines!!
    return a*b
x = multiply(3,4)
print(x)
