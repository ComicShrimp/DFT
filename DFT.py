import math


def funcaoXn(m):
    resultado = [0, 1, 0, 0]
    return resultado[m]


usarGraph = False
if input('Usar Gráfico(Requer Maplotlib): ') == 's':
    import matplotlib.pyplot as plt
    usarGraph = True

quantidadeDePontos = int(input('Digite a Quantidade de Pontos: '))

senoGrafico = []
cossenoGrafico = []
for m in range(0, quantidadeDePontos):
    cosseno = seno = 0

    for n in range(0, quantidadeDePontos):
        # Calcula somente o valor de seno e cosseno, após isso, acrescentar j na hora de mostrar
        cosseno += math.cos((2 * math.pi * m * n) /
                            quantidadeDePontos) * funcaoXn(n)
        seno += math.sin((2 * math.pi * m * n) /
                         quantidadeDePontos) * funcaoXn(n)

    cossenoGrafico.append(cosseno)
    senoGrafico.append(seno)

    # Necessário por conta do sinal na equação
    seno = seno * -1
    print('X[{}] = {:^6.2f} {:>2} {:>6.2f}j'.format(
        m, cosseno, '+' if seno >= 0 else '-', seno if seno > 0 else seno * -1))

if usarGraph:
  # Grafico Parte Real
  plt.subplot(1, 2, 1)
  plt.title('Parte Real')
  plt.grid(True)
  plt.plot(cossenoGrafico, 'o--')

  # Gráfico Parte Imaginaria
  plt.subplot(1, 2, 2)
  plt.title('Parte Imaginária')
  plt.grid(True)
  plt.plot(senoGrafico, color='tab:orange', linestyle = '--', marker='o')

  # Apresenta o Gráfico
  plt.show()
