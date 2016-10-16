#! /usr/bin/env python

""" Class to allow enumeration within Python 2.7. """

# Author: Matt Struble
# Date: Oct. 15 2016
#---------------------------------------------------------------------
import inspect

EXCLUDE_LIST = [
    '__module__',
    '__doc__'
    ]

class EnumError(AttributeError): pass

class Enum(object):
    """ A user-defined type that consists of a set of named constants that are known as enumerators.

    Examples:
        >>> class Key(Enum):
                A = 0
                B = 1
                C = 2

        >>> print Key.A
        Key.A
        >>> Key.A.value
        0
        >>> Key.A == 0
        True
        >>> Key.A == Key
        True
        >>> Key.A in Key
        True
        

        >>> test = Enum('Test', 'A', 'B', C=4)

        >>> print test.A
        Test.A
        >>> test.A.value
        0
        >>> test.B.value
        1
        >>> test.C.value
        4
        >>> test.A in test
        True
        >>> test.A == test
        True

        >>> test.A == Key.A
        False
        >>> test.A in Key
        False
        >>> Key.A in test
        False
    """      
        
    def __new__(self, name, *args, **kwargs):
        """ Creates automatic enumerated values for inline declarations.

            Takes in an unspecified length list of strings and/or keyword arguments
            to transform into enumerated values. The basic arguments will be
            automatically assigned (int) values ranging from 0..N based upon their order and
            keyword arguments will maintain their passed in values.
            
            Parameters
            ----------
                name : string
                    Name of the enumeration class to be created. Must start with an alpha value.
                *args : string
                    List of arguments to turn into enumerated values.
                **kwargs
                    List of keyword arguments to turn into enumerated values.

            Returns
            -------
                Enum: A generated enumerated type based upon inputted parameters.

            Raises
            ------
                TypeError
                    If name or *args are not string
                EnumError
                    If *args begin with a non-alpha value.
            
        """
        if not isinstance(name, basestring):
            raise TypeError("Enum name must be a string.")
        if not all(isinstance(arg, basestring) for arg in args):
            raise TypeError("Enum unnamed arguments must all be strings.")
        if not all(arg[0].isalpha() for arg in args):
            raise EnumError("Enum arguments must start with an alpha character.")
        
        enums = dict(zip(args, range(len(args))), **kwargs)
        return type(name, (Enum, ), enums)
    
    class __metaclass__(type):
        def __init__(self, *members):
            """ Automatically creates enumeration based upon class member variables.

                Iterates through the object's member list and replaces each member variable
                with an enumerated instance of that variable. 
            """
            if self.__name__ == 'Enum':
                return

            for item in self.__dict__:
                if item not in EXCLUDE_LIST:
                    eInstance = EnumInstance(self.__name__, item, self.__dict__.get(item))
                    setattr(self, item, eInstance)
                
       
        def __iter__(self):
            """ Returns a generator for enum values.

            When iterating the enum, only returns class members whose
            value are instances of EnumInstance.
            """
            return (self.__dict__[item] for item in self.__dict__ if isinstance(self.__dict__[item], EnumInstance))
        
        def __repr__(self):
            s = self.__name__
            if self.__bases__:
                s = s + '(' + ', '.join(map(lambda x : x.__name__, self.__bases__)) + ')'

            return s


class EnumInstance(object):
    """ Instance class for each enumerated value within Enum.

    EnumInstance enables enums to maintain their original class value for
    comparisons and reference while coding.

    Attributes:
        value : Value of the enum variable
    """

    def __init__(self, classname, enumname, value):
        self.__name__ = classname
        self.__classname = classname
        self.__enumname = enumname
        self.__value = value
        self.value = value;

    def __repr__(self):
        return "EnumInstance(%r, %r, %r)" % (self.__classname,
                                             self.__enumname,
                                             self.__value)
                    
    def __str__(self):
        return "%s.%s" % (self.__classname, self.__enumname)

    def __cmp__(self, other):
        """ Handles class, EnumInstance, and value comparisons for EnumInstance.

            If comparing to Class object it checks to see if the object's name matches
            the enum classname.

            If comparing to EnumInstance object it checks to see if the object's name
            matches the enum classname.

            Otherwise it compares the stored value with the value passed in.
        """
        if inspect.isclass(other) and issubclass(other, Enum):
            return cmp(self.__classname, other.__name__)
        elif isinstance(other, EnumInstance):
            return cmp(self.__classname, other.__name__)
        return cmp(self.__value, other)
