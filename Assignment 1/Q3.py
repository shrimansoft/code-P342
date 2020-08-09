
coutn = 0.0
i = 1.0
while (1/i) > 0.001 :
    coutn+= (1/i)
    i = i + 1;     
print("sum over 1+1/2 + 1/3 + ... till the sum does not change by more than 0.001 is : ", coutn)