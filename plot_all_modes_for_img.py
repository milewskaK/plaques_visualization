import numpy
import numpy as np
import csv
import matplotlib.pyplot as plt

#
# #wczytanie z pliku csv
import glob
# import pandas as pd
# #####wykres dla każdego z trybów dla każdego obrazu - czyli disc dla 4 obrazow jakie jest #####
#
# def readcsv(filename):
#     ifile = open(filename, "rU")
#     reader = csv.reader(ifile, delimiter=" ")
#                         #quoting=csv.QUOTE_NONNUMERIC)
#
#     rownum = 0
#     a = []
#
#     for row in reader:
#         a.append(row)
#         rownum += 1
#
#     ifile.close()
#     return a
# # #discnormal
# # daneH16 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/discnorm/Log_plakiH16_dn_1_SDA_discnormalise_SDAr_14.csv')
# # daneXY25 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/testXY25/discnormal/Log_plakiXY25_dn_1_SDA_discnormalise_SDAr_29.csv')
# # daneXY27 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/Log_plaki_dn_1_SDA_discnormalise_SDAr_25.csv')
# # daneZ15 = readcsv('C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/discnorm/Log_plakiZ15_dn_1_SDA_discnormalise_SDAr_18.csv')
# #
# # daneH16 = numpy.asarray(daneH16)
# # daneH16 = daneH16[:,4:15:2]
# # diceH16 = daneH16[:,4].astype(numpy.float)
# # sdarH16 = daneH16[:,0].astype(numpy.float)
# # #sdatH16 = daneH16[:,1].astype(numpy.float)
# # print(type(diceH16))
# #
# # daneXY25 = numpy.asarray(daneXY25)
# # daneXY25 = daneXY25[:,4:15:2]
# # diceXY25 = daneXY25[:,4].astype(numpy.float)
# # sdarXY25 = daneXY25[:,0].astype(numpy.float)
# # sdatXY25 = daneXY25[:,1].astype(numpy.float)
# # print(type(diceXY25))
# #
# # daneXY27 = numpy.asarray(daneXY27)
# # daneXY27 = daneXY27[:,4:15:2]
# # diceXY27 = daneXY27[:,4].astype(numpy.float)
# # sdarXY27 = daneXY27[:,0].astype(numpy.float)
# # sdatXY27 = daneXY27[:,1].astype(numpy.float)
# # print(type(diceXY27))
# #
# # daneZ15 = numpy.asarray(daneZ15)
# # daneZ15 = daneZ15[:,4:15:2]
# # diceZ15 = daneZ15[:,4].astype(numpy.float)
# # sdarZ15 = daneZ15[:,0].astype(numpy.float)
# # sdatZ15 = daneZ15[:,1].astype(numpy.float)
# # print(type(diceZ15))
# #
#
# ###########################SNOWFLAKE########################
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflake/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plaki_so_1_SDA_snowflake_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="XY27")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflake XY27", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/testXY25/snowflake/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiXY25_so_1_SDA_snowflake_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="XY25")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflake XY25", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/snowflake/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiH16_so_1_SDA_snowflake_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflakenormal: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="H16")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflake H16", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/snowflake/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiZ15_so_1_SDA_snowflake_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="Z15")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflake Z15", marker = 'o')
# plt.axis([0,100,0,0.5])
# plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla Snowflake")
# plt.xlabel("SDAr")
# plt.ylabel("DICE")
# plt.legend()
# plt.show()
#
# ######################SNOWFLAKENORMAL#####################################
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/snowflakenorm/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plaki_sn_1_SDA_snowflakenormalise_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="XY27")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflakenormal XY27", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/testXY25/snowflakenorm/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiXY25_sn_1_SDA_snowflakenormalise_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="XY25")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflakenormal XY25", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/snowflakenorm/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiH16_sn_1_SDA_snowflakenormalise_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflakenormal: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="H16")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflakenormal H16", marker = 'o')
# plt.axis([0,100,0,0.6])
#
# max_dice = []
# directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/snowflakenorm/'
# for i in range(101):
#     for file_name in glob.glob(directoryPath +'Log_plakiZ15_sn_1_SDA_snowflakenormalise_SDAr_' + str(i) +'.csv'):
#         dane = np.genfromtxt(file_name,delimiter=' ')
#         # do your calculations
#         dane = np.asarray(dane)
#         dane2 = dane[:,4:15:2]
#         #print(dane)
#         dice = dane2[:,4].astype(np.float)
#         #print(dice)
#     #binth = dane[:,2].astype(np.float)
#     #sdat = dane[:,1].astype(np.float)
#         y = max(dice)
#         #print('DISC, max dice ', y, np.argmax(dice))
#         max_dice.append(y)
#
# max_dice = np.asarray(max_dice)
# print("Max DICE snowflake: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))
#
# #plot 2d max dice dla każdego sdar
# plt.plot(max_dice, label="Z15")
# plt.plot(np.argmax(max_dice),max(max_dice),label="Max Snowflakenormal Z15", marker = 'o')
# plt.axis([0,100,0,0.5])
# plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla Snowflakenormalise")
# plt.xlabel("SDAr")
# plt.ylabel("DICE")
# plt.legend()
# plt.show()
#
# ##################################discnormal###################################################
#
max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_XY27_SDA_full/discnormal/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plaki_dn_1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
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
print("Max DICE d: ", np.max(max_dice), ' dla SDAr ', np.argmax(max_dice))

#plot 2d max dice dla każdego sdar
plt.plot(max_dice, label="XY27")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal XY27", marker = 'o')
plt.axis([0,100,0,0.6])

max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/testXY25/discnormal/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plakiXY25_dn_1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
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
plt.plot(max_dice, label="XY25")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal XY25", marker = 'o')
plt.axis([0,100,0,0.6])

max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testH16_full/discnorm/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plakiH16_dn_1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
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
plt.plot(max_dice, label="H16")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal H16", marker = 'o')
plt.axis([0,100,0,0.6])

max_dice = []
directoryPath = 'C:/Users/milka/PycharmProjects/plaki_wykresy/plaki_testZ15/discnorm/'
for i in range(101):
    for file_name in glob.glob(directoryPath +'Log_plakiZ15_dn_1_SDA_discnormalise_SDAr_' + str(i) +'.csv'):
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
plt.plot(max_dice, label="Z15")
plt.plot(np.argmax(max_dice),max(max_dice),label="Max Discnormal Z15", marker = 'o')
plt.axis([0,100,0,0.6])
plt.title("Wykres zależności dokładności algorytmu od promienia SDA dla Discnormalise")
plt.xlabel("SDAr")
plt.ylabel("DICE")
plt.legend()
plt.show()