# user-defined function
def greeting():
    print("Hello world")


greeting()  # Calling a function


def add():
    print(5 + 8)


add()

# paramaters and arguments
def student(firstname, course, age):
    print(firstname, course, age)

student("job","Datascience","23")
student("kate","computerscience","20")
student("joe","MIT","28")

#Built-infunctions
y= max(89,78,23,13,70)
print(y)

x= min(67,98,54,30)
print(x)

z= pow(2,3)
print(z)