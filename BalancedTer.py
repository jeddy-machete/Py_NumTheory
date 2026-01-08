#computes balanced ternary
#Nice lil recursive alg...see inductive proofs lol

def dec_to_balancedTer(n):
    sign = 1 if (n >= 0) else -1
    res = [] #little-endian, LSD first

    symbols = {1: "1",
               0: "0",
               2: "T"}

    def loop(cur):
        nonlocal res

        q = cur // 3
        r = cur % 3
        if (q == 0) and (r != 2):
            res.append(symbols[r])
            return
        elif (r == 2):
            res.append(symbols[r])
            loop(q + 1)
        else:
            res.append(symbols[r])
            loop(q)

    loop(abs(n))

    if sign == -1:
        for i in range(len(res)):
            if res[i] == "1":
                res[i] = "T"
            elif res[i] == "T":
                res[i] = "1"

    return "".join(res[::-1]) # return big endian

def balancedTer_to_dec(s):
    res = 0

    values = {"0" : 0,
              "1" : 1,
              "T" : -1}

    for i, digit in enumerate(s[::-1]):
        res += values[digit] * (3 ** i)

    return res
