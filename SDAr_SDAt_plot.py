import numpy
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#wczytanie z pliku csv
import glob
import pandas as pd
def readcsv(filename):
    ifile = open(filename, "rU")
    reader = csv.reader(ifile, delimiter=" ")
                        #quoting=csv.QUOTE_NONNUMERIC)

    rownum = 0
    a = []

    for row in reader:
        a.append(row)
        rownum += 1

    ifile.close()
    return a

max_dice = []
sdar_max_dice = []
sdat_max_dice = []

# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/'
#directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/discnorm/'
#directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/discnorm/'
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_wiekszy_zakres/'

# name = 'Log_plaki_dn_1_SDA_discnormalise_SDAr_'
#name = 'Log_plakiH16_dn_1_SDA_discnormalise_SDAr_'
#name = 'Log_plakiZ15_dn_1_SDA_discnormalise_SDAr_'
name = 'Log_XY27_plaki_dn_max__1_SDA_discnormalise_SDAr_'

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline4 = []  # os na gorze - dice
xline4 = []
yline4 = []
ax.set_xlabel('SDAt')
ax.set_ylabel('SDAr')
ax.set_zlabel('DICE Coefficient')
ax.scatter(xline4,yline4, zline4, c=zline4, cmap='summer', label='Discnormalise - Image A - bigger range')
ax.legend()
for i in range(201):
    for file_name in glob.glob(directoryPath + name + str(i) +'.csv'):
        dane = np.genfromtxt(file_name,delimiter=' ')
        # do your calculations
        dane = np.asarray(dane)
        dane = dane[:,4:15:2]
        #print(dane)
        dice = dane[:,4].astype(np.float)
        sdat = dane[:,1].astype(np.float)
        sdar = dane[:,0].astype(np.float)


        zline4 = dice[::150] # os na gorze - dice
        xline4 = sdat[::150]
        yline4 = sdar[::150]
        ax.scatter(xline4,yline4, zline4,c=zline4)


plt.show()

