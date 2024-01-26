#!/usr/bin/python3
"""This is a function running a class attribute"""

def hi(obj):
    """
    This object calls the attribute of the instance of a class Root

    Args:
        obj - thi is the instance of the class

    Return:
        This returns integer
    """
    print("You are " + obj.name)
class Robot:
    pass
x = Robot()
x.name = "Wavin"
hi(x)


