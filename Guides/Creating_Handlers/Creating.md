# Creating A Handler

Every handler is essentially a class that does something. Simple as that.

All handlers MUST inherit ‘BaseHandler’! If you attempt to load an object that does not inherit ‘BaseHandler’, then an exception will be raised!

This is the one and only restriction to handlers. The reason why this is the case is because cursepy must guarantee that a ‘handel()’ method is present on the object to load (You will find out why this is later). It is also important for the HandlerCollection(HC), as it will assign some values in the object, and cursepy does not want weird errors to occur.

## Python Inheritance and Classes

The handlers are a set of classes that inherit from a parent class which is a very powerful feature in Python and its object oriented programming.
It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

```python
#Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
#Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
```

Like in the ``handler_ex_1.py`` example, the BaseClass is imported from the cursepy.handlers.base file and having the BaseClass imported into the file of the handler.
The DerivedClass is processed in the current handler file where the functionality of the class is formulated. (``class DummyHand(BaseHandler)``)