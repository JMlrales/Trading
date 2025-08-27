def fact(n):
         if n<0:
                 return('El resultado es indefinido')
         elif n<=1:
                 return 1
         else:
                 return n*fact*(n-1)