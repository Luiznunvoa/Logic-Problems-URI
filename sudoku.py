n = int(input(''))
sudokus = []

for i in range(n):
    sudoku = []
    for _ in range(9):
        linha = list(map(int, input().split()))
        sudoku.append(linha)
    sudokus.append(sudoku)

numeros = set(range(1, 10))

for idx, sudoku in enumerate(sudokus, 1):
    valido = "SIM"
    
    for linha in sudoku:
        if set(linha) != numeros:
            valido = "NAO"
            break

    for coluna in zip(*sudoku):
        if set(coluna) != numeros:
            valido = "NAO"
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = []
            for x in range(3):
                for y in range(3):
                    bloco.append(sudoku[i + x][j + y])
            if set(bloco) != numeros:
                valido = "NAO"
                break

    print(f'Instancia {idx}\n{valido}\n')
