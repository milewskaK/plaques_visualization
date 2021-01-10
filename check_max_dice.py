import numpy as np
import csv
import matplotlib.pyplot as plt

#wczytanie z pliku csv
import glob
import pandas as pd

# for i in range(201):
#     i = str(i)
#     read_file = pd.read_csv (r'C:\Users\milka\PycharmProjects\plaki_wykresy\plaki_XY27_SDA_wiekszy_zakres\Log_XY27_plaki_dn_max__1_SDA_discnormalise_SDAr_' + i + '.txt')
#     read_file.to_csv (r'C:\Users\milka\PycharmProjects\plaki_wykresy\plaki_XY27_SDA_wiekszy_zakres\Log_XY27_plaki_dn_max__1_SDA_discnormalise_SDAr_' + i + '.csv', index=None)

max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_wiekszy_zakres/'
for i in range(101):

    for file_name in glob.glob(directoryPath +'Log_XY27_plaki_dn_max__1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
        dane = np.genfromtxt(file_name,delimiter=' ')
        # do your calculations
        dane = np.asarray(dane)
        dane2 = dane[:,4:15:2]
        # print(dane)
        dice = dane2[:,4].astype(np.float)
        jacc = dane2[:,5].astype(np.float)
        # print(dice)
        binth = dane2[:,2].astype(np.float)
        sdat = dane2[:,1].astype(np.float)
        # print(binth)
        y = max(dice)
        print('disc SDAr {}'.format(i), 'binthreshold {}'.format(binth[np.argmax(dice)]),
              'SDAt {}'.format(sdat[np.argmax(dice)]), 'MAX DICE {}'.format(y), 'JACC {}'.format(jacc[np.argmax(dice)]))

        max_dice.append(y)


max_dice = np.asarray(max_dice)
print('MAX MAX DICE: {} dla SDAr {}'.format(max(max_dice), np.argmax(max_dice)))


