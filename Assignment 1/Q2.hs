import Control.Monad ()
-- * main function     
main :: IO()
main = do 
    print " Factorail of 10 is : "       
    print $ factorial 10 
    print " Factorail of 15 is : " 
    print $ factorial 15   
    print " Factorail of 5 is  : " 
    print $ factorial 5 
    print " Factorail of -5 is : " 
    print $ factorial (-5) 
-- ^ there I run some test sample for function factorial.

-- * factorial 
factorial :: (Ord a, Num a, Enum a) => a -> Maybe a
factorial num = if num < 0 then Nothing else Just $product [1..num]
-- ^ this function return Nothing if input in nagative else it return Just (factorial of that number) 