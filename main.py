# 1.
for i in range(1, 11):
    print(i)

# 2.
for i in range(2, 21, 2):
    print(i)

# 3.
for _ in range(5):
    print("Salam dünya")

# 4.
i = 0
while i < 10:
    print(i)
    i += 1

# 5.
word = input("Söz: ")
for ch in word:
    print(ch)

# 6
for i in range(10, 0, -1):
    print(i)

# 7
    s = input("Daxil et: ")
    if s == "stop":
        break

# 8.
for i in range(1, 6):
    print(i, "→", i*i)

# 9
n = int(input("Say: "))
for _ in range(n):
    print("OK")

# 10.
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# 11
s = 0
for i in range(1, 101):
    s += i
print("Cəm:", s)

# 12
fact = 1
for i in range(1, 11):
    fact *= i
print("Faktorial:", fact)

# 13
total = 0
for _ in range(5):
    total += float(input("Ədəd: "))
print("Orta:", total / 5)

# 14
n = int(input("Ədəd: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# 15
count = 0
i = 1
while count < 10:
    print(i)
    i += 2
    count += 1

# 16
s = input("Söz: ")
saitler = "aeiouəöüı"
cnt = 0
for ch in s:
    if ch.lower() in saitler:
        cnt += 1
print("Sait sayı:", cnt)

# 17
n = input("Ədəd: ")
s = 0
for d in n:
    s += int(d)
print(s)

# 18
for i in range(1, 6):
    print(i, "→", i*i)

# 19
n = input("Ədəd: ")
print(n[::-1])

# 20
n = int(input("Ədəd: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Sadədir" if is_prime else "Sadə deyil")

# 21
for n in range(2, 101):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n)

# 22
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# 23
while True:
    s = input("Ədəd: ")
    if s == "exit":
        break
    print(int(s)**2)

# 24
for i in range(1, 1001):
    if sum(int(d) for d in str(i)) == 10:
        print(i)

# 25
n = input("Ədəd: ")
print(n.count("0"))

# 26
s = input("Söz: ")
print(s[::-1])

# 27
while True:
    x = int(input("Ədəd: "))
    if x == 0:
        break

# 28
s = input("Söz: ")
print(s.count("a"))

# 29
for i in range(1, 101):
    if i % 21 == 0:
        print(i)

# 30
N = int(input("N: "))
s = 0
for i in range(1, N+1):
    s += i
print("Cəm:", s)
