import random
sort = random.randint(1, 5)
num = int(input("digite um número "))
if num == sort:
    print("você ganhou")
else: print("você perdeu")
print(f"o numero sorteado foi: {sort}")
