def almost_double_factorial(n):
    summa = 1
    for i in range(1,(n+1),2):
        summa = summa*i      
    return summa
