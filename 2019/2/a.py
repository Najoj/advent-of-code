with open('input-a.txt', 'r') as file:
        #with open('test.txt', 'r') as file:
        code = file.read()


code = list(map(int, code.split(',')))
code[1] = 12
code[2] = 2

for i in range(0,len(code),4):
        cmd = code[i]
        if cmd == 1:
                code[code[i+3]] = code[code[i+1]]+code[code[i+2]]
        elif cmd == 2:
                code[code[i+3]] = code[code[i+1]]*code[code[i+2]]
        elif cmd == 99:
                break
        else:
                print('hurr durr bug')
print('svar', code[0])        
