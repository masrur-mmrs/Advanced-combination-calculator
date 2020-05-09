from fractions import Fraction
while True:
    n = float(input("Please enter n :) \n"))
    r = float(input("Please enter r :) \n"))
    z = r
    total = 1
    d = 1
    while r>=1:
        r = r-1
        total = total*(n-r)

    while z >= 1:
        d = d*(z)
        z = z-1
    ans = total/d
    frac = Fraction(ans)
    print("Answer is ",frac, "\n")
