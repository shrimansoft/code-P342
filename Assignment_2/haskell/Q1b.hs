
main::IO()
main = print $ averageDistance setPoints

setPoints :: [(Double,Double)]
setPoints = [(x,y)|x<-[1..6],y<-[1..6]]

averageDistance :: [(Double,Double)] -> Double
averageDistance nums = sum [abs(x1-x2)+abs(y1-y2)| (x1,y1) <- nums, (x2,y2) <- nums] / (36*36)


