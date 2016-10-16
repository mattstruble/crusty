#! /usr/bin/env python

""" Class to allow enumeration within Python 2.7. """

# Author: Matt Struble
# Date: Oct. 15 2016
#---------------------------------------------------------------------
import inspect

class Enum(object):
    class EnumError(TypeError): pass #base exception class
    
    class __metaclass__(type):
        def __init__(self, *members):
            if self.__name__ == 'Enum':
                return
            self.__dict = {}
            for item in self.__dict__:
                eInstance = EnumInstance(self.__name__, item, self.__dict__.get(item))
                setattr(self, item, eInstance)

        #def __setattr__(self, name, value):
        #    if name in self.__dict__:
        #        raise self.EnumError("Can't change %s.%s" % (self.__name__, name))
       
        def __iter__(self):
            for item in self.__dict__:
                yield self.__dict__[item]
        
        def __repr__(self):
            s = self.__name__
            if self.__bases__:
                s = s + '(' + ', '.join(map(lambda x : x.__name__, self.__bases__)) + ')'

            return s


class EnumInstance(object):

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
        if inspect.isclass(other) and issubclass(other, Enum):
            return cmp(self.__classname, other.__name__)
        
        return cmp(self.__value, other)

