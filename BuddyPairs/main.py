def buddy(start, limit):
    for n in range(start, limit):
        m = aliquot_sum(n)
        if m > n:
            if aliquot_sum(m) == n:
                return [n, m]
    return "Nothing"


def aliquot_sum(x):
    return sum(set(d for pair in ([i, x//i] for i in range(1, int(x**0.5)+1) if not x % i) for d in pair)) - x -1

