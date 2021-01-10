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

file_list = glob.glob("C:/Users/milka/PycharmProjects/plaki_wykresy/XY27_LN_SDA_BESTDICE/*.csv")
# print(file_list)
sigma_1 = []
sigma_2 = []
sdar = []
sdat = []
dice = []
# dane_all = []

for file_name in range(len(file_list)):
    dane = readcsv(file_list[file_name])
    dane = dane[1]
    if dane[5] == '':
        dane.pop(5)
    dane = np.asarray(dane)


    print(dane[5])
    dice.append(dane[5])
    sigma_1.append(dane[0])
    sigma_2.append(dane[1])
#     # dice.append(dice_x)
    sdar.append(dane[2])
    sdat.append(dane[3])
# #     # print('DISC, max dice ', y, np.argmax(dice))
# # dane_all = np.asarray(dane_all)
# # print(dane_all)
#
dice = np.asarray(dice)
sigma_1 = np.asarray(sigma_1)
sigma_2 = np.asarray(sigma_2)
sdar = np.asarray(sdar)
sdat = np.asarray(sdat)
#
#
dice = dice[:].astype(np.float)
sigma_1 = sigma_1[:].astype(np.float)
sigma_2 = sigma_2[:].astype(np.float)
sdar = sdar[:].astype(np.float)
sdat = sdat[:].astype(np.float)
#
#
# print(type(sigma_1[3]))
# print(type(sigma_2))
# # print(dane_all.shape)
# # #sigma1,sigma2,dice
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# zline = dice #os na gorze - dice
# xline = sdar
# yline = sdat
# #
# #
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zline2 = dice #os na gorze - dice
xline2 = sigma_1
yline2 = sigma_2
# #
# ax.scatter(yline,xline, zline, color = 'y', label='LN + SDA Discnormalise image A', alpha=0.3)
ax.scatter(yline2,xline2, zline2, color='r',label='LN sigma1 and sigma2', alpha=0.3)
ax.set_xlabel('Sigma1')
ax.set_ylabel('Sigma2')
ax.set_zlabel('DICE Coefficient')
ax.legend()
# # #ax.set_title("Porównanie dokładności detekcji plaków (DICE) w zależności od SDAt oraz Binthreshold \n dla różnych trybów (Obraz Z15)")
plt.show()



#plt.scatter(sdar, dice)


#plt.show()

#sigma1, sigma2, dice 2D
plt.scatter(sigma_1, dice, label="Sigma1", alpha=0.5)
plt.scatter(sigma_2, dice, label="Sigma2", marker = 'o', alpha=0.5)
plt.xlabel("LN Sigma values")
plt.ylabel("Dice Coefficient")
plt.legend()
plt.show()