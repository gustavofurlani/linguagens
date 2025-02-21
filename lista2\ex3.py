idade = int(input("digite sua idade: "))

if idade < 18 :
    print(f"menor de idade")
elif idade >=18 and idade <=59:
    print(f"adulto")
else:
    print(f"idoso")
