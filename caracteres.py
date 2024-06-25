import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""


rango= int(input("¿cuantos caracteres tendria la contraseña?"))

for i in range(rango):
    password += random.choice(caracteres)

print(password)
