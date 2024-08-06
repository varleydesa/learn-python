num_recebido = input("Digite um número Natural > 0: ")

num_recebido_int = int(num_recebido)

for dividendo in range(2, num_recebido_int+1):
    num_divisores = 0
    
    for divisor in range(1, dividendo+1):
        if(dividendo % divisor == 0):
            num_divisores = num_divisores + 1
    
    if(num_divisores == 2):
        print(dividendo)