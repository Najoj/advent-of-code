def next():
        for a in range(0,100):
                for b in range(0,100):
                        yield a,b
answer = 19690720

for a,b in next():
    with open('input-b.txt', 'r') as file:
        code = file.read()


    code = list(map(int, code.split(',')))
    code[1] = a
    code[2] = b

    for i in range(0,len(code),4):
        cmd = code[i]
        if cmd == 1:
                code[code[i+3]] = code[code[i+1]]+code[code[i+2]]
        elif cmd == 2:
                code[code[i+3]] = code[code[i+1]]*code[code[i+2]]
        elif cmd == 99:
                if code[0] == answer:
                        print('svar', code[1], code[2])        
                        print('svar', 100*code[1] + code[2])        
                        break

