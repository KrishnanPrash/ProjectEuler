# Problem100-Arranged_Probability

# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, 
# it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
# is a box containing eighty-five blue discs and thirty-five red discs.

# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, 
# determine the number of blue discs that the box would contain.


from math import sqrt


def isSq(x):
    sq = int(sqrt(x))
    return (sq*sq == x)

def dis(x):
    return 2*(x)*(x-1) + 1

isSquare = False
t = 10**12
# t = 50
iterations = 0

val = 1414213562372

# while not isSquare:
#     t += 1
#     isSquare = isSq(dis(t))
#     iterations += 1
#     if iterations % 1000000 == 0:
#         print(iterations, "Still Running...")


print("Total Number of Balls =",t)
print("Total Number of Blue Balls =",(-1+sqrt(dis(t)))/2)
