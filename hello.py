# hello.py


def add(m, n):
    s = m
    s += n
    return s


a = 2
b = 1

if a > 1:
    print('big')
    for i in range(1, 10):
        print('-->', i)

print('end')
print(add(2, 3))
