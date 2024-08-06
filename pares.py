num = input("Digite um número: ")

num_int = int(num)

for i in range(0, num_int+1):
    if(i % 2 == 0):
        print(i)
