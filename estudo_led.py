import matplotlib.pyplot as plt

fatias = [30, 10, 18, 20, 12, 10]
atividades = ['Amanhecer na Led', 'Pintura Moderna na Arena Show', 'Gritar "JAMAL"', 'Dormir pensando na Xacrinha', 'Rir Igual o Iven', 'Fuma maconha com o Pelé']
cores = ['yellow', 'black', 'brown', 'royalblue', 'orange', 'green']

textprops = {'fontsize':14}
plt.pie(fatias, labels = atividades, colors = cores, startangle= 90, shadow = True, \
        explode = (0, 0, 0.2, 0, 0, 0), autopct='%1.0f%%', textprops=textprops)
plt.show()
