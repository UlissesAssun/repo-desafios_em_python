limite = int(input("Digite o limite\n")) #Define o numero que não deve ser excedido
num1 = 0 #Variável que representa o primeiro numero
num2 = 1 #Variável que representa o segundo numero
soma = int #Soma dos dois numeros
listaDValores = []

while num2 <= limite: #Laço que só para de funcionar quando o 
    
    listaDValores.append(num2) #adiciona num2 a lista sempre que o laço se repete
    soma=num1+num2 #soma recebe a soma de num1 e num2
    num1=num2 #num1 recebe o valor de num2
    num2=soma #num2 recebe o valor de soma
    
print(listaDValores)