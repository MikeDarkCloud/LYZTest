def counter():
    count = 0
    def inc():
        nonlocal count
        count +=1
        return count
    return inc


foo = counter()
print(foo())
print(foo())
print(foo())

