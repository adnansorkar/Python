print()
print("This is a string", "Hello, World!", sep=": ")
print("This is a digit", 42)
print("This is a float:", 3.14)
print("This is a boolean:", True)
print("This is a list:", [1, 2, 3])
print("This is a tuple:", (1, 2, 3))
print("This is a dictionary:", {"a": 1, "b": 2})
print("This is a set:", {1, 2, 3})
print("This is a NoneType:", None)
print("This is a complex number:", 1 + 2j)
print("This is sum of 2 and 3:", 2 + 3)
print("This is a substraction of 5 and 3:", 5 - 3)
print("This is product of 2 and 3:", 2 * 3)
print("This is division of 6 by 3:", 6 / 3)
print("This is integer division of 7 by 3:", 7 // 3)
print("This is modulus of 7 by 3:", 7 % 3)
print("This is exponentiation of 2 to the power of 3:", 2 ** 3)
print("This is a comparison of 2 and 3:", 2 != 3)
print("This is a comparison of 2 and 3:", 2 >= 3)
print("This is a root of 16:", 16 ** 0.5)
print()

print()
name = "Adnan"
name2 = "Udoy"
age = 23
age2 = age + 2
price = 19.99
price2 = 29.99
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
print("My name and age is respectively:", name2, age2)
print(f"The price of the item is ${price:.2f}.")
print("The price of the second item is:", price2)
print()
