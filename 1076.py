a = input()
b = input()
c = input()
lst = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
x = str(lst.index(a))+str(lst.index(b))
x = int(x)
print(x * 10**lst.index(c))