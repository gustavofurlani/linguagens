nota1 = float(input("digite a primeira nota"))

nota2 = float(input("digite a segunda nota"))

total  = nota1 + nota2 

media = total /2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")
