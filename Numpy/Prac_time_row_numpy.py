import numpy as np

# sales = np.array([120, 135, 150, 160, 145, 130, 125, 155, 170, 185, 190, 175])
# moving_everage = np.convolve(sales, np.ones(6)/6, mode='valid')
# print(moving_everage)

# temps = np.array([5, 7, 12, 18, 23, 27, 30, 29, 24, 17, 10, 6])
# mean_tems = np.mean(temps)
# print(temps < mean_tems)

# тренд
# visitors = np.array([50, 55, 53, 60, 65, 63, 70, 72, 75, 78])
# days = np.arange(1,len(visitors) + 1)
# trend =  np.polyfit(days, visitors, 1)
# print(trend)

#Автокорреляция
# sales = np.array([120, 135, 150, 160, 145, 130, 125, 155, 170, 185, 190, 175])
# lag=0
# res = np.corrcoef(sales[:-lag], sales[lag:])[0, 1]
# print(res)

# anomals
# temps = np.array([30, 32, 35, 36, 38, 40, 41, 50, 42, 39, 37, 35])
# print(abs(temps-np.mean(temps))<np.var(temps)*2)

#Прогнозирование с использованием простого метода
# sales = np.array([120, 135, 150, 160, 145, 130, 125, 155, 170, 185, 190, 175])
# print(np.mean(sales[-3:]))
