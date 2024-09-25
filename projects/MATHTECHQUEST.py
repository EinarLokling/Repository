import itertools

digits = [str(num) for num in range (10)]

combinations = itertools.permutations(digits)

solutions = []

for n, comb in enumerate(combinations):
    a, b, c, d, e, f, g, h, i, j = comb
    abc = int(a + b + c)
    de = int(d + e)
    fgh = int(f + g + h)
    ij = int(i + j)
    
    res = abc * de - fgh * ij
    
    if res == 0:
        solutions.append(comb)
       # print(f"{abc}, {de}, {fgh}, {ij} = {res}")
    
