# -*- coding: utf-8 -*-
"""Historical Hourly Weather Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p31Pp_AQiPyycMoJOHEb9SIZptPQbZ_9

[ChatGPT](https://chatgpt.com/c/66fd464d-9abc-8003-9eac-9c7cc47547e2?model=gpt-4o)
"""

import pandas as pd

# Wczytaj plik temperature.csv
df_temperature = pd.read_csv('temperature.csv')

# Sprawdź pierwsze 5 wierszy
df_temperature.head()

df_temperature.info()

df_temperature.describe()

unique_cities = df_temperature.columns[1:]  # Zakładam, że pierwsza kolumna to czas, więc reszta to miasta
print(unique_cities)

avg_temperature = df_temperature.mean(numeric_only=True)
print(avg_temperature)

import matplotlib.pyplot as plt

# Wybierz trzy miasta
selected_cities = ['city_1', 'city_2', 'city_3']  # Zmień na rzeczywiste nazwy miast

# Narysuj wykres
df_temperature.plot(x='datetime', y=selected_cities, figsize=(10,6))
plt.title('Zmiany temperatury w wybranych miastach')
plt.xlabel('Czas')
plt.ylabel('Temperatura')
plt.show()

print(df_temperature.columns)

import matplotlib.pyplot as plt

# Wybierz kilka miast
selected_cities = ['Los Angeles', 'New York', 'Chicago']

# Narysuj wykres
df_temperature.plot(x='datetime', y=selected_cities, figsize=(10,6))
plt.title('Zmiany temperatury w wybranych miastach')
plt.xlabel('Czas')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)  # Obrót etykiet na osi X dla lepszej czytelności
plt.show()

# Konwersja temperatury z Kelvinów na Celsjusza
df_temperature[selected_cities] = df_temperature[selected_cities] - 273.15

# Narysuj wykres po konwersji
df_temperature.plot(x='datetime', y=selected_cities, figsize=(10,6))
plt.title('Zmiany temperatury w wybranych miastach (Celsjusz)')
plt.xlabel('Czas')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.show()

