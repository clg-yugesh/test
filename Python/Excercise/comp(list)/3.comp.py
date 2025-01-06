#Create a list of even numbers squared and odd numbers cubed from 1 to 10

x = [num**2 if num % 2 == 0 else num **3 for num in range(1,11)]

print(x)

