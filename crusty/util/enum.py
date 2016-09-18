
#! /usr/bin/env python

""" Class to allow enumeration within Python 2.7. """

# Author: Matt Struble
# Date: Sep. 19 2016
#---------------------------------------------------------------------
class Enum(type):

    def __init__(self, name, bases, dict):
        for base in bases:
            if base.__class__ is not EnumMetaClass:
                raise TypeError, "Enumeration base class must be enumeration"
        bases = filter(lambda x: x is not Enum, bases)
        self.__name__ = name
        self.__bases__ = bases
        self.__dict = {}
        for key, value in dict.items():
            self.__dict[key] = EnumInstance(name, key, value)

    def __getattr__(self, name):
        if name == '__members__':
            return self.__dict.keys()

        try:
            return self.__dict[name]
        except KeyError:
            for base in self.__bases__:
                try:
                    return getattr(base, name)
                except AttributeError:
                    continue

        raise AttributeError, name

    def __repr__(self):
        s = self.__name__
        if self.__bases__:
            s = s + '(' + string.join(map(lambda x: x.__name__,
                                          self.__bases__), ", ") + ')'
        if self.__dict:
            list = []
            for key, value in self.__dict.items():
                list.append("%s: %s" % (key, int(value)))
            s = "%s: {%s}" % (s, string.join(list, ", "))
        return s


class EnumInstance:

    def __init__(self, classname, enumname, value):
        self.__classname = classname
        self.__enumname = enumname
        self.__value = value

    def __int__(self):
        return self.__value

    def __repr__(self):
        return "EnumInstance(%r, %r, %r)" % (self.__classname,
                                             self.__enumname,
                                             self.__value)

    def __str__(self):
        return "%s.%s" % (self.__classname, self.__enumname)

    def __cmp__(self, other):
        return cmp(self.__value, int(other))

