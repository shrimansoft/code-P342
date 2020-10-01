#------------------------------* main function *-------------------
# this function will run some test
def main():
    v1 = [1,2,-2] 
    v2 = [2,5,3]
    v3 = [3,-4,-2]
    v4 = [-3,6,0]
    print( "product of (1,2,-2) and (2,5,3)")
    print(  dotProduct(v1,v2)) # printing the dot Product between V_1 and V_2.
    print(  "Vacter sum  of (1,2,-2) and (2,5,3)")
    print(  vacterSum(v1,v2))  # printing the sum between V_1 and V_2.
    print(  "product of (3,-4,-2) and (-3,6,0)")
    print(  dotProduct(v3,v4)) # printing the dot Product between V_3 and V_4.
    print(  "Vacter sum  of (3,-4,-2) and (-3,6,0)")
    print(  vacterSum(v3,v4)) # printing the sum between V_3 and V_4.

#---------------------------* vacterSum function *-----------------
# this functin will calculate the vecter sum.
def vacterSum(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
#-------------------------* dotProduct function *----------------------
# this function will calculate the dot product.
def dotProduct(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

if __name__ == "__main__":
    main()

#----------------* Output of the code is *------------------
# product of (1,2,-2) and (2,5,3)
# 6
# Vacter sum  of (1,2,-2) and (2,5,3)
# [3, 7, 1]
# product of (3,-4,-2) and (-3,6,0)
# -33
# Vacter sum  of (3,-4,-2) and (-3,6,0)
# [0, 2, -2]