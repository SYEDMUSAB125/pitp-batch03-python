# Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.
 

## Creating a Class:
Let us now create a class using the class keyword.
 
```python
class Details:
    name = "Ahmed"
    age = 20
 ```

## Creating an Object:
Object is the instance of the class used to access the properties of the class
Now lets create an object of the class.

### Example:
```python
obj1 = Details() 
```

Now we can print values:

### Example:
```python
class Details:
    name = "Ahmed"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)
```
### Output:
```
Ahmed
20
```



# self parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition. 

 

## Example:
```python
class Details:
    name = "Ahmed"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()
 
```
## Output:
```
My name is Ahmed and I'm 20 years old.
```
