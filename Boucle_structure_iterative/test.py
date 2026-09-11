"""def f1(liste: list) -> int:
    res = 0
    for i in liste:
        res += i 
    return res

print(f1([3, 1, 5]))

def f2(ch: str) -> str:
    res = ""
    for i in ch:
        res += i + "/"
    return res

print(f2(["Hello", "World", "!"]))

def f3(ln: list, n: int) -> list:
    res = []
    for i in ln:
        res.append(i * n)
    return res

print(f3([2,4,6],3))

def f4(tup: tuple) -> int:
    val_max = tup[0]
    for i in tup:
        if i > val_max:
            val_max = i
    return val_max

print(f4((3,8,7,1,4)))

def f5(chn: str) -> str:
    res = ""
    for i in chn:
        res = i + res
    return res

print(f5("python"))

def f6(n: int) -> int:
    res = 0
    for i in range(n):
        res += i
    return res

print(f6(5))

def f7(lst: list) -> list:
    res = []
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    return res

print([1,2,3,4,5,6,7])

def f8(ls: str) -> int:
    voyelles = "aeiouyAEIOUY"
    compte = 0
    for i in ls:
        if i in voyelles:
            compte += 1
    return compte

print(f8("Bonjour"))

def f9(lst: list) -> list:
    res = []
    for i in lst:
        res.append(i ** 2)
    return res

print(f9([1,2,3,4]))

def f10(a: int, b: int) -> tuple:
    res = []
    for i in range(a ,b):
        if i % 3 == 0:
            res.append(i)
    return tuple(res)

print(f10(3, 10))

def f11(a: int, b: int) -> int:
    res = 0
    for i in range(a, b, -2):
        res += i
    return res 

print(f11(10, 6))

def f12(a: int) -> int:
    res = 0
    for i in range(a):
        if i % 2 != 0:
            res += i
    return res

print(f12(6))

def f13(ch: list) -> None:
    for i in ch:
        print(i, end="/")

print(f13([1,2,3]))

def f14(a: int, b: int) -> int:
    for i in range(a, b):
        print(i*2, end=" ")

print(f14(2, 5))

def f15(sk: str) -> str:
    for i in sk:
        print(i*2, end="")

print(f15("Hello"))"""
