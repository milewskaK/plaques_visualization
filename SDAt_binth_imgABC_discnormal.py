
import numpy
import numpy as np
import csv
import matplotlib.pyplot as plt


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
#directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/'
#directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/discnorm/'
#directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/discnorm/'

#name = 'Log_plaki_dn_1_SDA_discnormalise_SDAr_'
#name = 'Log_plakiH16_dn_1_SDA_discnormalise_SDAr_'
#name = 'Log_plakiZ15_dn_1_SDA_discnormalise_SDAr_'


dane = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/Log_plaki_dn_1_SDA_discnormalise_SDAr_25.csv')
dane2 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/discnorm/Log_plakiH16_dn_1_SDA_discnormalise_SDAr_14.csv')
dane3 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/discnorm/Log_plakiZ15_dn_1_SDA_discnormalise_SDAr_18.csv')

dane = numpy.asarray(dane)
dane = dane[:,4:15:2]
dice = dane[:,4].astype(numpy.float)
binth = dane[:,2].astype(numpy.float)
sdat = dane[:,1].astype(numpy.float)
print(type(dice))

dane2 = numpy.asarray(dane2)
dane2 = dane2[:,4:15:2]
dice2 = dane2[:,4].astype(numpy.float)
binth2 = dane2[:,2].astype(numpy.float)
sdat2 = dane2[:,1].astype(numpy.float)
print(type(dice2))

dane3 = numpy.asarray(dane3)
dane3 = dane3[:,4:15:2]
dice3 = dane3[:,4].astype(numpy.float)
binth3 = dane3[:,2].astype(numpy.float)
sdat3 = dane3[:,1].astype(numpy.float)
print(type(dice3))



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline = dice[::20] #os na gorze - dice
xline = binth[::20]
yline = sdat[::20]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline2 = dice2[::20] #os na gorze - dice
xline2 = binth2[::20]
yline2 = sdat2[::20]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline3 = dice3[::20] #os na gorze - dice
xline3 = binth3[::20]
yline3 = sdat3[::20]


ax.scatter(yline,xline, zline,color = 'b', label='Image A', alpha=0.3 )
ax.scatter(yline2,xline2, zline2,color = 'c',label='Image B',alpha=0.3 )
ax.scatter(yline3,xline3, zline3, color = 'r', label='Image C',alpha=0.3)
ax.set_xlabel('SDAt')
ax.set_ylabel('binthreshold')
ax.set_zlabel('DICE Coefficient')
ax.legend()
#ax.set_title("Porównanie dokładności detekcji plaków (DICE) w zależności od SDAt oraz Binthreshold \n dla różnych trybów (Obraz XY27)")

plt.show()