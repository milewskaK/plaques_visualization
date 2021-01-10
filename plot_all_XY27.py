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

#discnormal
max_dice = []

directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plaki_dn_1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
        dane = np.genfromtxt(file_name,delimiter=' ')
        # do your calculations
        dane = np.asarray(dane)
        dane = dane[:,4:15:2]
        #print(dane)
        dice = dane[:,4].astype(np.float)
        #print(dice)
        #binth = dane[:,2].astype(np.float)
        #sdat = dane[:,1].astype(np.float)
        y = max(dice)
        #print('DISC, max dice ', y, np.argmax(dice))
        max_dice.append(y)

max_dice = np.asarray(max_dice)
print("Max DICE Discnormal: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))

#plot 2d max dice dla każdego sdar
plt.plot(max_dice, label="Discnormal")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal", marker = 'o')
plt.axis([0,100,0,0.5])
#plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla różnych trybów")


#snowflake
max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflake/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plaki_so_1_SDA_snowflake_SDAr_' + str(i) +'.csv'):
        dane = np.genfromtxt(file_name,delimiter=' ')
        # do your calculations
        dane = np.asarray(dane)
        dane2 = dane[:,4:15:2]
        #print(dane)
        dice = dane2[:,4].astype(np.float)
        #print(dice)
    #binth = dane[:,2].astype(np.float)
    #sdat = dane[:,1].astype(np.float)
        y = max(dice)
        #print('DISC, max dice ', y, np.argmax(dice))
        max_dice.append(y)

max_dice = np.asarray(max_dice)
print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))

#plot 2d max dice dla każdego sdar
plt.plot(max_dice, label="Snowflake")
plt.plot(np.argmax(max_dice),max(max_dice), label=" Max Snowflake", marker = 'o')
plt.axis([0,100,0,0.5])
#plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla różnych trybów")

#snowflakenormal
max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflakenorm/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plaki_sn_1_SDA_snowflakenormalise_SDAr_' + str(i) +'.csv'):
        dane = np.genfromtxt(file_name,delimiter=' ')
        # do your calculations
        dane = np.asarray(dane)
        dane2 = dane[:,4:15:2]
        #print(dane)
        dice = dane2[:,4].astype(np.float)
        #print(dice)
    #binth = dane[:,2].astype(np.float)
    #sdat = dane[:,1].astype(np.float)
        y = max(dice)
        #print('DISC, max dice ', y, np.argmax(dice))
        max_dice.append(y)

max_dice = np.asarray(max_dice)
print("Max DICE snowflakenormal: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))

#plot 2d max dice dla każdego sdar
plt.plot(max_dice, label="Snowflakenormal")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflakenormal", marker = 'o')
plt.axis([0,100,0,0.5])
#plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla różnych trybów")
plt.xlabel("SDAr")
plt.ylabel("DICE")
plt.legend()
plt.show()

##############plot all - 3d porownanie trybow ############################

#wczytanie z pliku csv

# #wczytanie do array
dane = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/Log_plaki_dn_1_SDA_discnormalise_SDAr_25.csv')
dane2 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflake/Log_plaki_so_1_SDA_snowflake_SDAr_29.csv')
dane3 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflakenorm/Log_plaki_sn_1_SDA_snowflakenormalise_SDAr_28.csv')

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


ax.scatter(yline,xline, zline,label='Discnormalise' )
ax.scatter(yline2,xline2, zline2,label='Snowflake' )
ax.scatter(yline3,xline3, zline3,label='Snowflakenormalise')
ax.set_xlabel('SDAt')
ax.set_ylabel('binthreshold')
ax.set_zlabel('DICE Coefficient')
ax.legend()
#ax.set_title("Porównanie dokładności detekcji plaków (DICE) w zależności od SDAt oraz Binthreshold \n dla różnych trybów (Obraz XY27)")

plt.show()