mat1 = []

print("Введите числа матрицы, разделяя их пробелом")
firstStr = input("")

firstStr = firstStr.split(' ')
size = len(firstStr)
mat1.append(firstStr)

for e in range(size - 1):
        mat1.append(input().split(' '))

##matr = [['3', '2', '5', '4'],
##         ['2', '3', '6', '8'],
##         ['1', '-6', '-9', '-20'],
##         ['4', '1', '4', '0']]



def opred(mat):
    size = len(mat[0])
    

    for e in mat:
        for i in range(len(e)):
            e[i] = float(e[i])

    for e in mat:
        print(e)

    print("\n")

    minor = [[mat]]
    chisla = [[1]]
    i = 0

    if size > 2:
        size1 = size
        while size1 != 2: # Перебираем матрицы разного размера
            minor.append([])
            chisla.append([])
            i += 1
            i1 = i
            size2 = size1
            r = 0
            for e in range(len(minor[i - 1])):# Перебираем все матрицы ранее
                #print(len(minor[i - 1]))
                for g in range(size2):# Перебераем строку конкретной матрицы
                    minor[i].append([])# Матрица
                    chisla[i].append(minor[i - 1][e][0][g] * -1 if g % 2 == 1 else minor[i - 1][e][0][g])
                    for stroka in range(1, size2):
                        minor[i][(r * (size2)) + g].append([])
                        for el in range(len(minor[i - 1][e][stroka])):
                            if stroka != 0 and el != g:
                                minor[i][(r * (size2)) + g][stroka - 1].append(minor[i - 1][e][stroka][el])
                r += 1
            size1 -= 1
        #for e in minor:
            #for i in e:
                #for g in i:
                    #print(g)
                #print(" ")
            #print("\n\n")

        opr = 0
        opred = []
        opred1 = []
        for e in range(len(minor[i1])):
            opred.append(minor[i1][e][0][0] * minor[i1][e][1][1] - minor[i1][e][0][1] * minor[i1][e][1][0])
        for e in range(len(chisla) - 1, 0, -1):
            for i in range(len(chisla[e])):
                opred[i] = opred[i] * chisla[e][i]
                try:
                    #print(i // int((len(chisla[e])) / (len(chisla[e-1]))), " ", opred[i])
                    opred1[i // int((len(chisla[e])) / (len(chisla[e-1])))] += opred[i]
                    #print(opred1[i // int((len(chisla[e])) / (len(chisla[e-1])))])
                except IndexError:
                    opred1.append(0)
                    opred1[i // int((len(chisla[e]))/(len(chisla[e-1])))] += opred[i]
            opred = opred1
            print(opred1)
            opred1 = []
        print("Определитель: ",opred[0])
        
            
            

    elif size == 2:
        opr = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        opr = mat[0][0]

##for e in range(20):
##    matr[3][3] = str(e)
##    opred(matr)

opred(mat1)
