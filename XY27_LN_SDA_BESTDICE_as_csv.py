import numpy as np
import csv
import matplotlib.pyplot as plt

#wczytanie z pliku csv
import glob
import pandas as pd



# #for i in range(101):
#     #i = str(i)
#     read_file = pd.read_csv (r'C:\Users\milka\PycharmProjects\plaki_wykresy\plaki_testH16_full\disc\Log_plakiH16_do_1_SDA_disc_SDAr_' + i + '.txt')
#     read_file.to_csv (r'C:\Users\milka\PycharmProjects\plaki_wykresy\plaki_testH16_full\disc\Log_plakiH16_do_1_SDA_disc_SDAr_' + i + '.csv', index=None)
#C:\Users\milka\PycharmProjects\plaki_wykresy\XY27_LN_SDA_BESTDICE\plaki_LN_SDA__1_1_SDA_discnormalise_SDAr_1_SDAt_2_BEST_DICE.txt
file_list = glob.glob("C:/Users/milka/PycharmProjects/plaki_wykresy/XY27_LN_SDA_BESTDICE/*.txt")
print(file_list)

for i in range(len(file_list)):
     read_file = pd.read_csv (file_list[i])
     read_file.to_csv (file_list[i].replace('.txt','') + '.csv', index=None)
