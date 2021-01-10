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


# #plot 2d max dice dla każdego sdar
plt.plot(max_dice, label="Discnormal")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal", marker = 'o')
plt.axis([0,100,0,0.5])
plt.xlabel("SDAr")
plt.ylabel("DICE")
plt.legend()

# #wczytanie do array
dane = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_wiekszy_zakres/Log_XY27_plaki_dn_max__1_SDA_discnormalise_SDAr_25.csv')

dane = numpy.asarray(dane)
dane = dane[:,4:15:2]
dice = dane[:,4].astype(numpy.float)
binth = dane[:,2].astype(numpy.float)
sdat = dane[:,1].astype(numpy.float)
print(type(dice))



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline = dice[::20] #os na gorze - dice
xline = binth[::20]
yline = sdat[::20]


ax.scatter(yline,xline, zline,label='Discnormalise' )

ax.set_xlabel('SDAt')
ax.set_ylabel('binthreshold')
ax.set_zlabel('DICE Coefficient')
ax.legend()

plt.show()