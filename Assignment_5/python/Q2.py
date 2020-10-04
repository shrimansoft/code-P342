from lib.My_library import *

def main():
    polynomialAsList=[1,-3,-7,27,-18]
    LaguerreRootOfPolynomial_method(polynomialAsList,0.00001,0.000001,"Assignment_5/python/Q2_data/LaguerreRoot_data.txt")

if __name__ == "__main__":
    main()

# code output
# ---* Root of Polynomials method *--
# Enter your Guss : 3
# 3.0000000001666662
# 3.0000000000000018
# number of Itretion 2
# root of the equation is  3.0000000000000018 with error  1e-06  .
# ---* Root of Polynomials method *--
# Enter your Guss : 3
# 2.038359371683079
# 2.000008903654634
# 2.000000000106839
# 1.9999999999999971
# number of Itretion 4
# root of the equation is  1.9999999999999971 with error  1e-06  .
# ---* Root of Polynomials method *--
# Enter your Guss : 3
# 1.0000049172683183
# 1.0000000000122942
# 1.000000000000001
# number of Itretion 3
# root of the equation is  1.000000000000001 with error  1e-06  .
# ---* Root of Polynomials method *--
# Enter your Guss : 3
# -3.0000000002271463
# -3.0
# number of Itretion 2
# root of the equation is  -3.0 with error  1e-06  .
# Roots of the polynomial are  [3.0000000000000018, 1.9999999999999971, 1.000000000000001, -3.0]  with error  1e-06