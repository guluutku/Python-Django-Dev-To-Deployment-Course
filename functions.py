
# Different from other langs. Python uses identation with tabs and spaces. No brackets, curly brackets

# Create Function
def sayHello():
    print('Hello')

sayHello()
print('----------------------')

def sayHello2(name = 'Sam'):
    print('Hello ' + name)

sayHello2()
sayHello2('Beth')
print('----------------------')

# Return
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(1, 2))
print('----------------------')
print()
print()

# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(2,3))
print('----------------------')
