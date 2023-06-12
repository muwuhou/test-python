import PyQt6.QtWidgets
from PyQt6.QtCore import QObject
import inspect


clazz_table = {}  # str -> set[str]
def walk():
    for name in dir(PyQt6.QtWidgets):
        obj = getattr(PyQt6.QtWidgets, name)
        if inspect.isclass(obj):
            walk_inheritance_chain(obj)


def walk_inheritance_chain(clazz):
    #if clazz is QObject:
    #    return
    for base in clazz.__bases__:
        if base not in clazz_table:
            clazz_table[base] = set([clazz])
        else:
            clazz_table[base].add(clazz)
        walk_inheritance_chain(base)


def dump():
    for key in clazz_table:
        print(key.__name__)
        for subclass in clazz_table[key]:
            print("\t", subclass.__name__)        

walk()
dump()            
