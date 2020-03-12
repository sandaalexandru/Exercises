# Verificare string folosind while

user_input = ""
while user_input != "telacad":
    user_input = input("Introduce-ti string-ul telacad: " )
print("Sfarsitul programului")

# Suma utilizator input
while True:
    n = input("Introduce-ti un numar: ")
    if int(n) > 2:
        break
a = 0
for i in range(int(n)+1):
    a = a + i
print(a)

# Comparare

x = 2 + 3j

if isinstance(x, int):
    print(x+3)
elif isinstance(x, float):
    print(x/2)
elif isinstance(x, complex):
    print(x.imag)
    print(x.real)
    print(abs(x))
else:
    print("nimic nu se potriveste")

# Numere pare/impare

n = int(input("Introdu un numar: "))
if n%2 == 0:
    print("numarul este par")
else:
    print("numarul este impar")

# Numar prim

num = 8
numarprime = "prime"
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            numarprime = "notprime"
            print("Numarul se-nparte la " + str(i))
            break
    if numarprime == "prime":
        print("Numarul este prim")
    else:
        print("Numarul nu este prim")
else:
    print("Numarul nu este prim")