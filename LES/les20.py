def mul(a):
    def helper(b):
        return a * b
    return helper

mul5 = mul(5)
print(mul5(10)) # = 50
