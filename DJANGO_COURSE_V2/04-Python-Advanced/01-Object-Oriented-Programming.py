# Object Oriented Programming
# 
# Object Oriented Programming (OOP) tends to be one of the major obstacles for recruits when they are first starting to learn Python.
# 
# For this lesson we will construct our knowledge of OOP in Python by building on the following topics:
# 
# * Objects
# * Using the *class* keyword
# * Creating class attributes
# * Creating methods in a class
# * Learning about Inheritance
# * Learning about Special Methods for classes
# 
# Lets start the lesson by remembering about the Basic Python Objects. For example:

# In[1]:


mylist = [1,2,3]


# Remember how we could call methods on a list?

# In[2]:


mylist.count(2)


# What we will basically be doing in this lecture is exploring how we could create an Object type like a list. We've already learned about how to create functions for repeatable sections of code. Using Object Oriented Programming will allow us to create Objects that we can import into other scripts and allow us to scale our projects even larger. We will start by exploring Objects in general.
# 
# ## Objects
# 
# In Python, *everything is an object*. Remember from previous lectures we can use type() to check the type of object something is:

# In[4]:


print(type(1))
print(type([]))
print(type(()))
print(type({}))


# So we know all these things are objects, so how can we create our own Object types? That is where the *class* keyword comes in.
# 
# ## class
# 
# The user defined objects are created using the class keyword. The class is a blueprint that defines a nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object 'l' which was an instance of a list object. 
# 
# Let see how we can use **class**:

# In[6]:


# Create a new object type called Sample
class Sample():
    pass

# Instance of Sample
x = Sample()

print(type(x))


# By convention we give classes a name that starts with a capital letter. Note how x is now the reference to our new instance of a Sample class. In other words, we **instantiate** the Sample class.
# 
# Inside of the class we currently just have pass. But we can define class attributes and methods.
# 
# An **attribute** is a characteristic of an object.
# A **method** is an operation we can perform with the object.
# 
# For example we can create a class called Agent. An attribute of an Agent may be their height, eye color, name, etc. A method is typically more similar to a function acting on the object itself, for example having the Agent object print out its code name would be suitable for a method.
# 
# Let's get a better understanding of attributes through an example.
# 
# ## Attributes
# The syntax for creating an attribute is:
#     
#     self.attribute = something
#     
# There is a special method called:
# 
#     __init__()
# 
# This method is used to initialize the attributes of an object. For example:

# In[7]:


class Agent():
    def __init__(self,real_name):
        self.real_name = real_name


# In[8]:


Agent


# In[10]:


# Need to provide the arguments!
m = Agent()


# In[11]:


m = Agent('Mike')


# In[13]:


a = Agent('Alice')


# Lets break down what we have above.The special method 
# 
#     __init__() 
# is called automatically right after the object has been created:
# 
#     def __init__(self, real_name):
# Each attribute in a class definition begins with a reference to the instance object. It is by convention named self. The real_name is the argument. The value is passed during the class instantiation.
# 
#      self.real_name = real_name

# Now we have created two instances of the Agent class. With two Agent instances, they each have their own real_name attribute, we can then access these attributes like this:

# In[14]:


m.real_name


# In[15]:


a.real_name


# Note how we don't have any parenthesis after real_name, this is because it is an attribute and doesn't take any arguments.
# 
# In Python there are also *class object attributes*. These Class Object Attributes are the same for any instance of the class. For example, we could create the attribute **planet** for the Agent class. Agents (regardless of their height,eye color,name, or other attributes will always be on planet Earth, at least for now! We apply this logic in the following manner:

# In[16]:


class Agent():
    
    # Class Object Attribute
    planet = 'Earth'
    
    def __init__(self,real_name,eye_color,height):
        self.real_name = real_name
        self.eye_color = eye_color
        self.height = height


# In[17]:


m = Agent('Mike','Green',175)


# In[20]:


m.real_name


# In[22]:


m.height


# In[23]:


m.eye_color


# Note that the Class Object Attribute is defined outside of any methods in the class. Also by convention, we place them first before the init.

# In[19]:


m.planet


# ## Methods
# 
# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are essential in encapsulation concept of the OOP paradigm. This is essential in dividing responsibilities in programming, especially in large applications.
# 
# You can basically think of methods as functions acting on an Object that take the Object itself into account through its *self* argument.
# 
# Lets go through an example of creating a Circle class:

# In[1]:


class Circle():
    
    # Should be same for any circle of any size
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        return 2 * self.radius * Circle.pi


# In[5]:


c = Circle(radius=2)

print('Radius is: {}'.format(c.radius))


# In[8]:


# Notice how for a method we need the () to actually call the method!
print('Area is: {}'.format(c.area()))


# In[9]:


# Can reset the radius like this
c.radius = 10


# In[10]:


c.area()


# Notice how we used self. notation to reference attributes of the class within the method calls, also notice the difference in calling a method versus calling an attribute, methods need you to call with a () at the end otherwise they won't actually be executed.

# ## Inheritance
# 
# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).
# 
# Lets see an example by incorporating our previous work on two new classes:

# ** First Base Class**

class Person():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        print("I am {} {}.".format(self.first_name,self.last_name))

    def hello(self):
        print("Hello!")

 

class Agent(Person):
        
    def true_name(self,passcode):
        # We can add additional methods unique to the Agent class
        
        if passcode == 123:
            print("I am a secret agent!")
            print("I am {} {}.".format(self.first_name,self.last_name))
        else:
            self.report()
    
    def _private_methods(self):
        # Start methods with a single underscore to make them "private"
        # Keep in mind Python is very open by its nature
        # Any user could still find out these classes exist
        # This is more to denote that the user shouldn't be needing
        # To interact with this method.
        print("Privacy Please.")


john = Agent("john",'smith')
john.true_name(passcode=123)

# In[28]:


class Person():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        print("I am {} {}.".format(self.first_name,self.last_name))

    def hello(self):
        print("Hello!")


# ** Second Class will inherit from Person base class, allowing it to inherit its attributes and methods. Notice how we pass the class, we don't actually instantiate it with () , we just pass it through.**

# In[33]:


class Agent(Person):
    
    def __init__(self,first_name,last_name,code_name):
        Person.__init__(self,first_name,last_name)
        self.code_name = code_name

    def report(self):
        # This overwrites the Person report() method
        print('Sorry I can not give you my real name')
        print("You can call me {}".format(self.code_name))
        
    def true_name(self,passcode):
        # We can add additional methods unique to the Agent class
        
        if passcode == 123:
            print("Thank you for providing the passcode")
            print("I am {} {}.".format(self.first_name,self.last_name))
        else:
            self.report()
    
    def _private_methods(self):
        # Start methods with a single underscore to make them "private"
        # Keep in mind Python is very open by its nature
        # Any user could still find out these classes exist
        # This is more to denote that the user shouldn't be needing
        # To interact with this method.
        print("Privacy Please.")
        
        
        
    # Notice how we don't have the hello() method here
    # We will be inheriting it from the Person class!
    
            


# In[34]:


x = Agent(first_name='Alan',last_name='Turing',code_name='Hero')


# In[35]:


x.hello()


# In[36]:


# x.true_name(100)


# In[37]:


# x.true_name(123)


# In this example, we have two classes: Person and Agent. The Person is the base class, the Agent is the derived class. 
# 
# The derived class inherits the functionality of the base class. 
# 
# * It is shown by the hello() method. 
# 
# The derived class modifies existing behavior of the base class.
# 
# * shown by the report() method. 
# 
# Finally, the derived class extends the functionality of the base class, by defining a new true_name() method.

# ## Special Methods
# 
# Finally lets go over special methods. Let's imagine you wanted to check the length of a list, that is easy, you just call len() on that object. But what is the length of an Agent? Let's see what happens:

# # In[38]:


# len(x)


# Interesting, what if we try printing the Agent object?

# In[39]:


# print(x)


# In order to interact with Python's built in methods, we will need to use special method names that are built in to PYython. These are denoted by their use of double underscores on each side:

# Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example Lets create a Book class:



# class Book():
    
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return "Title: {} , author:{}, pages: {}.".format(self.title, self.author, self.pages)

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         print("A book is destroyed")


# # In[44]:


# book = Book("Python Rocks!", "Jose Portilla", 159)

# #Special Methods
# print(book)
# print(len(book))
# del book


#     The __init__(), __str__(), __len__() and the __del__() methods.
# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.
# 
 