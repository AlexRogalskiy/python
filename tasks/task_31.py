def arrayMultiply(array, c):
    return [element*c for element in array]

def arraySum(a, b):
    return map(sum, zip(a,b))

def intermediate(a, b, ratio):
    aComponent = arrayMultiply(a, ratio)
    bComponent = arrayMultiply(b, 1-ratio)
    return arraySum(aComponent, bComponent)

def gradient(a, b, steps):
    steps = [n/float(steps) for n in range(steps)]
    for step in steps:
        print intermediate(a, b, step)

#print arrayMultiply((1,2,3), 0.3)
#print arraySum((1,2,3), (0.5, 0.5, 0.5))
#print intermediate((1,2,3), (3,2,1), 0.5)
#print gradient(None, None, 5)


pureBlue = (8, 123, 157)
pureYellowGreen = (0,84,166)

gradient(pureBlue, pureYellowGreen, 6)

