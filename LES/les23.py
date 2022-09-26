class F:
    pass

class E(F):
    pass

class C(E):
    pass

class D(E):
    pass

class A(C, D):
    pass

class B(D):
    pass

print(A.__mro__)
