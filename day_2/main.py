suma_ids = 0

with open('day_2/input.txt', 'r') as file:
    ranges = file.read().strip().split(',')

#### Part 1
for r in ranges:
    start_str, end_str = r.split('-')
    start, end = int(start_str), int(end_str)

    for num in range(start, end + 1):
        
        s_num = str(num)
        length = len(s_num)

        if length % 2 != 0:
            continue
        
        mitad = length // 2
        
        if s_num[:mitad] == s_num[mitad:]:
            suma_ids += num

suma_ids_2 = 0
###### Part 2
for r in ranges:
    start_str, end_str = r.split('-')
    start, end = int(start_str), int(end_str)

    for num in range(start, end + 1):
        
        s_num = str(num)
        
        for n in range(2, len(s_num) + 1):
            length = len(s_num)

            if length % n != 0:
                continue
            part_size = len(s_num) // n
            
            parts = []

            for i in range(0, len(s_num), part_size):
                part = s_num[i:i+part_size]
                parts.append(part)
            
            result = all(x == parts[0] for x in parts)
            
            if result:
                suma_ids_2 += num
                break
print(suma_ids)
print(suma_ids_2)