try:
    num1=float(input("Donner un nomber entier : "))
    num2=float(input("Donner un autre nomber entier : "))
    res=num1/num2
    print(res)
except(ValueError,ZeroDivisionError):
    print("Désolé quelque chose ne s'est pas bien passé ")
    