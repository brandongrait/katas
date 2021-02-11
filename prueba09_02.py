test = "771-748-5508"
one = test.split("-")
aux = 0
for numbers in one:
    suma = sum(list(map(int,list(numbers))))
    aux += suma
print(aux)
