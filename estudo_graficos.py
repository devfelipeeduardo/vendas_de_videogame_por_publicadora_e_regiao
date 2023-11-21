import matplotlib.pyplot as plt

def grafico1():
    x, y = [2, 3, 5] , [3, 5, 7]

    plt.bar(x, y, label = 'Senta na pica')
    plt.legend()
    plt.xlabel('Variavel 1')
    plt.ylabel('Variavel 2')
    plt.title('Teste Plot')
    plt.show()

def grafico2():
    x1, y1 = [1, 2, 3], [4, 5, 6]
    x2, y2 = [2, 4, 6], [9, 3, 1]

    plt.bar(x1, y1, label = 'Lista 1', color = 'blue')
    plt.bar(x2, y2, label = 'Lista 2', color = 'red')
    plt.legend()
    plt.show()


idades = [902, 2, 9, 5, 5, 1, 4, 32]


def metodo_dificil():
    x = 0
    ids = []

    for x in range(len(idades)):
        if x == 0:
            ids.append(x)
        elif x == len(idades):
            break
        else:
            ids.append(x)

    print(ids)

# metodo_dificil()

def metodo_facil():
    ids = [x for x in range(len(idades))]

    print(ids)

metodo_facil()


# grafico1()
