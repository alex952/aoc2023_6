import math
import sys
import functools
import operator

with open(sys.argv[1]) as f:
    times = list(filter(lambda x: x, f.readline().strip().split(":")[1].split(" ")))
    distances = list(filter(lambda x: x, f.readline().strip().split(":")[1].split(" ")))


print(f"Times -> {times}")
print(f"Distances -> {distances}")


# Mathematical approach we can represent the inequality such as
# (t - x) * x > d
# tx - x**2 > d
# -x**2 + tx - d > 0

# Classic quadratic formula
# Coefficients would be:
# a = -1
# b = t
# c = -d
# Solve for x given that x needs to be integer the solutions
# solving for > 0 would be ceil of + side and floor of - side


def waysOfWinning(t: str, d: str) -> int:
    t = int(t)
    d = int(d)

    a = -1
    b = t
    c = -(
        d + 1
    )  # to acount for the fact that it's not a greater equals and they're integers

    sqr = math.sqrt(b**2 - 4 * a * c)
    xplus = (-b + sqr) / (2 * a)
    xminus = (-b - sqr) / (2 * a)

    print(xplus)
    print(xminus)

    ways = math.floor(xminus) - math.ceil(xplus) + 1

    print(f"Solutions for {t}ms and {d}mm -> {ways}")

    return ways


results = map(lambda x: waysOfWinning(x[0], x[1]), zip(times, distances))
result = functools.reduce(operator.mul, results)

print(f"Result part1 -> {result}")

t_p2 = "".join(times)
d_p2 = "".join(distances)

result = waysOfWinning(t_p2, d_p2)
print(f"Result part2 -> {result}")
