n = 5

print(f"\n1.")

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

print(f"\n2.")

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print(f"\n3.")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

print(f"\n4.")

for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end='')
    print()

print(f"\n5.")

for i in range(1, n+1):
    for j in range(i):
        print(f"{i}", end='')
    print()

print(f"\n6.")

for i in range(n, 0, -1):
    for j in range(i):
        print(f"{i}", end='')
    print()

print(f"\n7.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

print(f"\n8.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print(f"\n9.")

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print(f"\n10.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")