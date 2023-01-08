
v1 = [1, 3.2]
v2 = [5, 6]


def inner_product(v1, v2):
    a = 0
    if len(v1) != len(v2):
        print('Inner product not defined for vectors of different dimensions')
    else:
        for i in range(0, len(v1)):
            a += v1[i]*v2[i]
        return a


ipanswer = inner_product(v1, v2)
print(ipanswer)
