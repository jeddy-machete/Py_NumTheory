# implementation of exponentiation by repeated squaring
# Nothing really deep, just exponentiation by repeated squaring
# Its worth writing out since i'll prolly remember it more if i implement it
#   ...discrete math is hard

def fast_mod(base, expt, mod):
    if mod == 1:
        return 0

    base = base % mod
    res = 1


    while expt > 0:
        if ((expt & 1) == 1):
            res = (res * base) % mod

        base = (base * base) % mod
        expt = (expt >> 1)

    return res
