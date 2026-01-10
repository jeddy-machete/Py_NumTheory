#Format
#Each modulus equation will be represented as a tuple
#eg "x == 2 (mod 3)" -> (2, 3)

import math

def crt_wrapper(list_of_sys):
    return recurse_crt(list_of_sys[0],
                       list_of_sys[1:])

#all this function proves is that I read too much DPF last year...
def recurse_crt(cur_sys, list_of_sys):
    if not list_of_sys:
        return cur_sys
    else:
        next_sys = list_of_sys[0]

        if coprime(cur_sys, next_sys):
            return recurse_crt(compute_crt(cur_sys, next_sys),
                               list_of_sys[1:])
        else:
            if consistent_reduction(cur_sys, next_sys):
                return recurse_crt(compute_crt_noncoprime(cur_sys, next_sys),
                                   list_of_sys[1:])
            else:
                return "System is inconsistent"

def compute_crt(sys1, sys2):
    M = math.lcm(sys1[1], sys2[1])
    M1 = sys2[1]
    M2 = sys1[1]

    u_inv_1 = pow(M1, -1, sys1[1])
    u_inv_2 = pow(M2 , -1, sys2[1])

    a_fin = ((sys1[0] * M1 * u_inv_1) + (sys2[0] * M2 * u_inv_2)) % M
    return (a_fin, M)


#difficult to understand-ish
def compute_crt_noncoprime(sys1, sys2):
    a1, m1 =  sys1
    a2, m2 = sys2
    g = math.gcd(sys1[1], sys2[1])

    m1_reduced = m1 // g
    m2_reduced = m2 // g
    diff = (a2 - a1) % m2_reduced

    k = (diff * pow(m1_reduced, -1, m2_reduced)) % m2_reduced
    x = (a1 + m1 * k) % math.lcm(m1, m2)

    return (x, math.lcm(m1, m2))

#predicate for ease
def coprime(sys1, sys2):
    return math.gcd(sys1[1], sys2[1]) == 1


def consistent_reduction(sys1, sys2):
    g = math.gcd(sys1[1], sys2[1])
    return (sys1[0] % g) == (sys2[0] % g)


# crt_wrapper([(2, 3), (3, 5), (2, 7)])
# crt_wrapper([(5, 6), (4, 5), (3, 4), (2, 3)])
# crt_wrapper([(4, 6), (4, 5), (3, 4), (2, 3)])
# crt_wrapper([(0, 2), (0, 4), (0, 5)])
