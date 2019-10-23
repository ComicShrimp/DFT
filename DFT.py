import math


def funcaoXn(m):
    resultado = [0, 1, 0, 0]
    return resultado[m]


usarGraph = False
if input('Usar Gráfico(Requer Maplotlib) (S/N) : ') == 's':
    import matplotlib.pyplot as plt
    usarGraph = True

quantidadeDePontos = int(input('Digite a Quantidade de Pontos: '))

senoGrafico = []
cossenoGrafico = []
magnitudeGrafico = []
faseGrafico = []

print('Valor em X[m] | Magnitude | Fase')
for m in range(0, quantidadeDePontos):
    cosseno = seno = magnitude = fase = 0

    for n in range(0, quantidadeDePontos):
        # Calcula somente o valor de seno e cosseno, após isso, acrescentar j na hora de mostrar
        cosseno += math.cos((2 * math.pi * m * n) /
                            quantidadeDePontos) * funcaoXn(n)
        seno += math.sin((2 * math.pi * m * n) /
                         quantidadeDePontos) * funcaoXn(n)

    magnitude = math.sqrt(math.pow(cosseno, 2) + math.pow(seno, 2))
    try:
        fase = math.atan(seno / cosseno)
    except:
        fase = 0

    cossenoGrafico.append(cosseno)
    senoGrafico.append(seno)
    magnitudeGrafico.append(magnitude)
    faseGrafico.append(fase)

    # Necessário por conta do sinal na equação
    seno = seno * -1
    print('X[{}] = {:^6.2f} {:>2} {:>6.2f}j | Xm[{}] = {} | Xo[{}] = {}'.format(
        m, cosseno, '+' if seno >= 0 else '-', seno if seno > 0 else seno * -1, m, magnitude, m, fase))

if usarGraph:
    # Grafico Parte Real
    plt.subplot(2, 2, 1)
    plt.title('Parte Real')
    plt.grid(True)
    plt.plot(cossenoGrafico, 'o--')

    # Gráfico Parte Imaginaria
    plt.subplot(2, 2, 2)
    plt.title('Parte Imaginária')
    plt.grid(True)
    plt.plot(senoGrafico, color='tab:orange', linestyle='--', marker='o')

    # Grafico de Magnitude
    plt.subplot(2, 2, 3)
    plt.title('Magnitude')
    plt.grid(True)
    plt.plot(magnitudeGrafico, color='tab:red', linestyle='--', marker='o')

    # Gráfico de Fase
    plt.subplot(2, 2, 4)
    plt.title('Fase')
    plt.grid(True)
    plt.plot(faseGrafico, color='tab:green', linestyle='--', marker='o')

    # Apresenta o Gráfico
    plt.show()
