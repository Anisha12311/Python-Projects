with open('myfile.txt') as f:
    for line in f:
        print(line , end="")
        
        

print([number for number in range(1,20) if number%2 == 0])


t = ["Pythonista", 7, False, 3.14159]
print(type(t))

print(tuple(range(10)))

print(list(range(10)))

words = ("foo", "bar", "baz", "qux", "quux", "corge")

L1, *L2, L3 = words

print(L2)