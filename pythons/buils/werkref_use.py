import weakref


class A:
    pass


a = A()
ar = weakref.ref(a)

print(ar)
print(ar())

del a
print(ar)
print(ar())
