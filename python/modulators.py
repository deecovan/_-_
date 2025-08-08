import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Параметры
f_c = 10  # Частота несущей (Гц)
f_m = 1   # Частота модулирующего сигнала (Гц)
A_c = 1   # Амплитуда несущей
A_m = 0.5 # Амплитуда модулирующего сигнала
fs = 100  # Частота дискретизации (Гц)
T = 2     # Длительность сигнала (с)
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Модулирующий сигнал (синусоида)
message = A_m * np.sin(2 * np.pi * f_m * t)

# Несущая (синусоида)
carrier = A_c * np.sin(2 * np.pi * f_c * t)

# Амплитудная модуляция
am = (A_c + message) * np.sin(2 * np.pi * f_c * t)

# Частотная модуляция
# Угол фазы несущей зависит от модулирующего сигнала
kf = 5  # Коэффициент частотной девиации
fm = A_c * np.sin(2 * np.pi * f_c * t + kf * np.cumsum(message) / fs)


# Фазовая модуляция
# Изменение фазы несущей в зависимости от модулирующего сигнала
kp = 5  # Коэффициент фазовой девиации
pm = A_c * np.sin(2 * np.pi * f_c * t + kp * message)


# Отображение результатов
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, message)
plt.title('Модулирующий сигнал')

plt.subplot(4, 1, 2)
plt.plot(t, am)
plt.title('Амплитудно-модулированный сигнал (AM)')

plt.subplot(4, 1, 3)
plt.plot(t, fm)
plt.title('Частотно-модулированный сигнал (FM)')

plt.subplot(4, 1, 4)
plt.plot(t, pm)
plt.title('Фазово-модулированный сигнал (PM)')

plt.tight_layout()
plt.show()