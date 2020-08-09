main :: IO()
main = print $  sumM  $ break ( < 0.001 ) [1 / x | x <- [1 .. ]]


sumM :: (Foldable t, Num a) => (t a, b) -> a
sumM (xs,_) = sum xs