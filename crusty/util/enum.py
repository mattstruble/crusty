#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Oct. 15 2016
import inspect

class EnumError(AttributeError): pass

class _meta_enum(type):
    def __init__(cls, cls_name, cls_bases, cls_dict):
        """ Automatically creates enumeration based upon classes dictionary.

            Iterates through the object's member list and replaces each member variable
            with an enumerated instance of that variable. 
        """
        if cls_name == 'Enum':
            return
        
        for item in cls_dict:
            if type(cls_dict.get(item)) != staticmethod: # preserve static methods
                if item[0].isalpha(): # Only enumerate 'public' variables
                    eInstance = EnumInstance(cls_name, item, cls_dict.get(item))
                    setattr(cls, item, eInstance)

        cls._initialized = True

    def __setattr__(cls, attr, value):
        """ Raises EnumError if attempting to change an attribute at runtime. """
        if hasattr(cls, '_initialized'):
            raise EnumError("type object '%s' is an enumeration and cannot be modified at runtime." % cls.__name__)

        super(_meta_enum, cls).__setattr__(attr, value)

       
    def __iter__(self):
        """ Returns a generator for enum values.

        When iterating the enum, only returns class members whose
        value are instances of EnumInstance.
        """
        return (self.__dict__[item] for item in self.__dict__ if not callable(item) and isinstance(self.__dict__[item], EnumInstance))
        
    def __repr__(self):
        s = self.__name__
        if self.__bases__:
            s = s + '(' + ', '.join(map(lambda x : x.__name__, self.__bases__)) + ')'

        return s

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
        >>> for key in Key: print key
        Key.A
        Key.B
        Key.C
        >>> Key.C - Key.B
        1
        (also works for: +, *, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |)
        

        >>> Test = Enum('Test', 'A', 'B', C=4)

        >>> print Test.A
        Test.A
        >>> Test.A.value
        0
        >>> Test.B.value
        1
        >>> Test.C.value
        4
        >>> Test.A in Test
        True
        >>> Test.A == Test
        True

        >>> Test.A == Key.A
        False
        >>> Test.A in Key
        False
        >>> Key.A in Test
        False
    """      
    __metaclass__ = _meta_enum
        
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
        self._initialized = True

    def __setattr__(self, value, attr):
        """ Raises EnumError if attempting to change an attribute at runtime. """
        if hasattr(self, '_initialized'):
            raise EnumError("type object '%s' is an enumeration and cannot be modified at runtime." % self.__classname)

        self.__dict__[value] = attr

    def __repr__(self):
        return "EnumInstance(%r, %r, %r)" % (self.__classname,
                                             self.__enumname,
                                             self.__value)
                    
    def __str__(self):
        return "%s.%s" % (self.__classname, self.__enumname)

    def __int__(self):
        return int(self.__value)

    def __float__(self):
        return float(self.__value)

    def __long__(self):
        return long(self.__value)

    def __oct__(self):
        return oct(self.__value)

    def __hex__(self):
        return hex(self.__value)

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
            if self.__classname == other.__name__:
                return cmp(self.value, other.value)
            else:
                return cmp(self.__classname, other.__name__)
        return cmp(self.__value, other)

    ## Left operand arithmetic operations

    def __add__(self, other):
        return self.__value + other

    def __sub__(self, other):
        return self.__value - other

    def __mul__(self, other):
        return self.__value * other

    def __div__(self, other):
        return self.__value / other

    def __floordiv__(self, other):
        return self.__value // other

    def __mod__(self, other):
        return self.__value % other

    def __divmod__(self, other):
        return divmod(self.__value, other)

    def __pow__(self, other, modulo=None):
        return pow(self.__value, other, modulo)

    def __lshift__(self, other):
        return self.__value << other

    def __rshift__(self, other):
        return self.__value >> other

    def __and__(self, other):
        return self.__value & other

    def __xor__(self, other):
        return self.__value ^ other

    def __or__(self, other):
        return self.__value | other

    ## Right operand arithmetic operations

    def __radd__(self, other):
        return other + self.__value

    def __rsub__(self, other):
        return other - self.__value

    def __rmul__(self, other):
        return other * self.__value

    def __rdiv__(self, other):
        return other / self.__value

    def __rfloordiv__(self, other):
        return other // self.__value

    def __rmod__(self, other):
        return other % self.__value

    def __rdivmod__(self, other):
        return divmod(other, self.__value)

    def __rpow__(self, other, modulo=None):
        return pow(other, self.__value, modulo)

    def __rlshift__(self, other):
        return other << self.__value

    def __rrshift__(self, other):
        return other >> self.__value

    def __rand__(self, other):
        return other & self.__value

    def __rxor__(self, other):
        return other ^ self.__value

    def __ror__(self, other):
        return other | self.__value

