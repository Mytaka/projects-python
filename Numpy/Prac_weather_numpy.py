import numpy as np

city1_temps = np.array([22, 22, 10, 15, 17, 11, 16, 25, 24, 11])
city2_temps = np.array([20, 22, 18, 18, 15, 10, 11, 10, 18, 12])

# city1_temps = np.array([26.5, 24.1, 26.8, 25.0, 23.0, 23.7, 22.9])
# city2_temps = np.array([25.3, 26.0, 24.5, 27.1, 25.0, 23.4, 24.8])

# print('everage temperature for city1: ', round(city1_temps.mean(),1), ' for city2: ', round(city2_temps.mean(),1))
# print('max temperature for city1: ', round(np.max(city1_temps),1), ' for city2: ', round(np.max(city2_temps),1))
# print('min temperature for city1: ', round(np.min(city1_temps),1), ' for city2: ', round(np.min(city2_temps),1))

# print('\n', 'diferent between max and min temperature of cities: ', 'city1: ', round(np.max(city1_temps)-np.min(city1_temps),1),' for city2: ', round(np.max(city2_temps)-np.min(city2_temps),1))

#дни когда в первом городе холоднее чем во втором
# colders_days = city1_temps < city2_temps
# a = np.where(colders_days == True)
# print(colders_days)

#Количество дней с температурой выше среднего:
# over_mean1 = np.sum(np.mean(city1_temps) < city1_temps)
# over_mean2 = np.sum(np.mean(city2_temps) < city2_temps)
# print(over_mean1, over_mean2)

#Скользящее среднее:
# filter = np.ones(3)/3
# moving_evegare1 = np.convolve(city1_temps, filter, mode='valid')
# moving_evegare2 = np.convolve(city2_temps, filter, mode='valid')
# print(moving_evegare1)
# print(moving_evegare2)

#Нормализация данных:
# normal_temperatyre1 =(city1_temps - np.min(city1_temps)) / (np.max(city1_temps) - np.min(city1_temps))
# normal_temperatyre2 =(city2_temps - np.min(city2_temps)) / (np.max(city2_temps) - np.min(city2_temps))
# print(normal_temperatyre1,'\n',normal_temperatyre2)

#анализ аномальных данных
# anomaly1 = abs(city1_temps - np.mean(city1_temps)) > np.var(city1_temps) * 2
# anomaly2 = abs(city2_temps - np.mean(city2_temps)) > np.var(city2_temps) * 2
# print(anomaly1, anomaly2)

# Корреляция температур между городами:
# corellation = np.corrcoef(city1_temps,city2_temps)[0,1]
# print(corellation)

