import math


def funcaoXn(m):
    if m == 0:
        return 1
    elif m == 1:
        return 2
    elif m == 2:
        return -1
    elif m == 3:
        return 1
    else:
        return 0


quantidadeDePontos = int(input('Digite a Quantidade de Pontos: '))

resultado = 0
for m in range(0, quantidadeDePontos):
    cosseno = seno = 0

    for n in range(0, quantidadeDePontos):
        # Calcula somente o valor de seno e cosseno, após isso, acrescentar j na hora de mostrar
        cosseno += math.cos((2 * math.pi * m * n) /
                            quantidadeDePontos) * funcaoXn(n)
        seno += math.sin((2 * math.pi * m * n) /
                         quantidadeDePontos) * funcaoXn(n)

    # Necessário por conta do sinal na equação
    seno = seno * -1
    print('X[{}] = {:^6.2f} {:>2} {:>6.2f}j'.format(
        m, cosseno, '+' if seno >= 0 else '-', seno if seno > 0 else seno * -1))
