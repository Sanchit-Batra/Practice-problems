from functools import reduce

if __name__ == '__main__':
    listu = []
    for i in range(100 + 1):
        j = i * i
        listu.append(j)
    s_of_sq = reduce(lambda x, y: x + y, listu)
    listy = [i for i in range(100 + 1)]
    rawsq_of_s = reduce(lambda x, y: x + y, listy)
    sq_of_s = rawsq_of_s * rawsq_of_s
    ans = sq_of_s - s_of_sq
    print(ans)

