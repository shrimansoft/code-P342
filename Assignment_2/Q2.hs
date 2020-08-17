main :: IO()
main = do 
    print "product of (1,2,-2) and (2,5,3)"
    print $ dotProduct (1,2,-2) (2,5,3)
    print "Vacter sum  of (1,2,-2) and (2,5,3)"
    print $ vacterSum (1,2,-2) (2,5,3)
    print "product of (3,-4,-2) and (-3,6,0)"
    print $ dotProduct (3,-4,-2) (-3,6,0)
    print "Vacter sum  of (3,-4,-2) and (-3,6,0)"
    print $ vacterSum (3,-4,-2) (-3,6,0)



dotProduct :: Num a => (a, a, a) -> (a, a, a) -> a
dotProduct (a1,a2,a3) (b1,b2,b3) = a1*b1+a2*b2+a3*b3

vacterSum :: (Num a, Num b, Num c) => (a, b, c) -> (a, b, c) -> (a, b, c)
vacterSum (a1,a2,a3) (b1,b2,b3) = (a1+b1,a2+b2,a3+b3)
