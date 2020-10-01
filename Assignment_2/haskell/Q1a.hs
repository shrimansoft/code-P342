main::IO()
main = print          -- using print funtrion to print the output of averageDistance Function.
    $ " Average Distance between points [1,2,3,4,5,6] is : " ++ show (averageDistance [1, 2, 3, 4, 5, 6])  -- calling averageDistance function with list of points as argument.

-- -----------------------* averageDistance function *-------------------------
-- this function take a list of 6 Double value and return average Distance( Double type) 
averageDistance :: [Double] -> Double
averageDistance nums = sum  -- sum function take a list and return the sum of all elemints in the list. 
    [abs (x - y) | x <- nums, y <- nums]    -- this is a list generator that produce 36 elements ( abs difference between points)
    / 36 -- finally we devide the sum by 36.

-- ------------------* output of the code *-----------------
-- " Average Distance between points [1,2,3,4,5,6] is : 1.9444444444444444"