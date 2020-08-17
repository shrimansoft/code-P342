main::IO()
main = print $ averageDistance [1, 2, 3, 4, 5, 6]


averageDistance :: [Double] -> Double
averageDistance nums = sum [abs (x - y) | x <- nums, y <- nums] / 36