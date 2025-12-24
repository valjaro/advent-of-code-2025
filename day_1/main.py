init = 50
count = 0
# Part 1
with open('input1.txt', 'r') as file:
    for line in file:
        val = int(line[1:]) 
        
        if line[0] == 'L':
            init -= val
        else:
            init += val
            
        init %= 100
        if init == 0:
            count += 1
print(count)
# Part 2
init = 50
count = 0

with open('input1.txt', 'r') as file:
    for line in file:
        val = int(line[1:])
        prev = init
        
        if line[0] == 'R':
            init += val
            # Fórmula para movimiento positivo
            # Cuántos múltiplos de 100 hay entre prev y init
            count += (init // 100) - (prev // 100)
            
        elif line[0] == 'L':
            init -= val
            # Fórmula para movimiento negativo
            # Usamos (x-1) para excluir el inicio y contar el fin si cae en 0
            count += ((prev - 1) // 100) - ((init - 1) // 100)

print(count)