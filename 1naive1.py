import sys
import functools
import operator

with open(sys.argv[1]) as f:
    times = list(filter(lambda x: x, f.readline().strip().split(":")[1].split(" ")))
    distances = list(filter(lambda x: x, f.readline().strip().split(":")[1].split(" ")))


print(f"Times -> {times}")
print(f"Distances -> {distances}")


def waysOfWinning(t, d):
    t = int(t)
    d = int(d)
    ways = 0

    for i in range(t + 1):
        button_pushed_ms = i + 1

        if (t - button_pushed_ms) * button_pushed_ms > d:
            ways += 1

    print(f"For {t}ms and {d}mm -> {ways} ways to win")
    return ways


results = map(lambda x: waysOfWinning(x[0], x[1]), zip(times, distances))
result = functools.reduce(operator.mul, results)

print(f"Result part1 -> {result}")

t_p2 = "".join(times)
d_p2 = "".join(distances)

result = waysOfWinning(t_p2, d_p2)
print(f"Result part2 -> {result}")
