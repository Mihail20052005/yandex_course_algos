inputfile = open('input.txt', 'rt')

data = [line.rstrip() for line in inputfile.readlines()]

rang = 10
n = int(data[0])
del data[0]

outputfile = open('output.txt', 'wt')

outputfile.write('Initial array:\n')
outputfile.write(', '.join(data) + '\n')
for i in range(len(data[0])):
    outputfile.write('**********\n')
    outputfile.write('Phase ' + str(i + 1) + '\n')
    b = [[] for k in range(rang)]
    for x in data:
        q = int(x) // 10 ** i % 10
        b[q].append(x)
    data = []
    for r in range(rang):
        data += b[r]
        outputfile.write('Bucket ' + str(r) + ': ')
        if len(b[r]) == 0:
            outputfile.write('empty\n')
        else:
            outputfile.write(', '.join(map(str, b[r])) + '\n')

outputfile.write('**********\n')
outputfile.write('Sorted array:\n')
outputfile.write(', '.join(data))