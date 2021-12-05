I = [line.rstrip() for line in open('input')]
numbers = I[0].split(',')

output = open('numbers', 'w')
for number in numbers:
    output.write(number+"\n")
output.close()

output = open('cards', 'w')
for i in range(2, len(I)):
    if (I[i] != ""):
        numbers = I[i].split()
        for number in numbers:
            output.write(number+"\n")
output.close()