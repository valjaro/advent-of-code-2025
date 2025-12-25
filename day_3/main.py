with open('day_3/input.txt', 'r') as file:
    banks = file.read().strip().split('\n')

joltage = 0
# banks = [
#     '987654321111111',
#     '811111111111119',
#     '234234234234278',
#     '818181911112111'
    
# ]
# Part 1
# for bank in banks:
#     m1, m2 = '0', '0'
#     p1, p2 = 0, 0
#     for i, n in enumerate(bank):
#         if n > m1:
#             if i != len(bank) - 1:
#                 m1 = n
#                 p1 = i
#     for j in range(p1 + 1, len(bank)):
#         if bank[j] > m2:
#             m2 = bank[j]
#             p2 = j
#     num_str = m1 + m2
#     joltage += int(num_str)

# print(joltage)

# Part 2
total_joltage = 0

for bank in banks:
    stack = []
    deletes = len(bank) - 12
    for num in bank:
        while stack and deletes > 0 and stack[-1] < num:
            stack.pop()            deletes -= 1
        
        stack.append(num)
    
    if deletes > 0:
        stack = stack[:-deletes]
        
    num_str = "".join(stack)

    total_joltage += int(num_str)

print(total_joltage)