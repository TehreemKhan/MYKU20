def getpPrimeList(start, end):
    l=list()
    for num in range(start, end):
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            l.append(num)
    return l

def storeResult(fileName, l):
    with open(fileName, "w") as f:
        f.write(str(l))

storeResult("results.txt",getpPrimeList(1,251))