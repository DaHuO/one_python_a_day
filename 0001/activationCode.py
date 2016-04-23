# -*- coding: UTF-8 -*-

import random
def activationCode():
    code_length = 6
    code_number = 200
    code_repository = []
    for i in range(code_number):
        code = ""
        while code == "":
            for i in range(code_length):
                num = int(random.random()*61)
                if num<10:
                    code += chr(num + 48)
                elif num < 36:
                    code += chr(num + 55)
                else:
                    code += chr(num + 61)
            if code in code_repository:
                code = ""
            else:
                code_repository.append(code)
    file_code = open("activation code", "w")
    for code in code_repository:
        file_code.write(code + '\n')
    file_code.close()

if __name__ == '__main__':
    activationCode()
