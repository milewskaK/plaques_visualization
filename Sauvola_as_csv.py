import numpy as np
import csv
import matplotlib.pyplot as plt

#wczytanie z pliku csv
import glob
import pandas as pd

file_list = glob.glob("C:/Users/milka/PycharmProjects/plaki_wykresy/Sauvola/*.txt")
print(file_list)

for i in range(len(file_list)):
     read_file = pd.read_csv (file_list[i])
     read_file.to_csv (file_list[i].replace('.txt','') + '.csv', index=None)