# Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:
# Types of access specifiers 
1.  Public access modifier
2. Private access modifier
3. Protected access modifier
   
# Public Access Specifier in Python
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
## Example:
```python
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"musab")
print(obj.age)
print(obj.name)
```
## Output:
```
21
musab
```

# Public Access Specifier in Python
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
## Example:
```python
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"musab")
print(obj.age)
print(obj.name)
```
## Output:
```
21
musab
```


# Protected Access Modifier  
In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member.
The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
## Example:
```python
class Student:
    def __init__(self):
        self._name = "musab"

    def _funName(self):      # protected method
        return "pitp"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 
```
## Output:
```
musab
pitp

musab
pitp
```
