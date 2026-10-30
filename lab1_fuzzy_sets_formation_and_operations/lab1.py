import os

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

os.makedirs("img", exist_ok=True) # папка для рисунків звіту
plt.rcParams["axes.grid"] = True # сітка на графіках


def finish(fig, name):
    """Зберегти рисунок у img/<name>.png і показати на екрані."""
    fig.tight_layout()
    fig.savefig(f"img/{name}.png", dpi=150)
    plt.show()

#Дві базові множини для операцій
x = np.linspace(0, 20, 401)
f1 = fuzz.gaussmf(x, 8, 2.5) # множина A: дзвін із центром 8 і σ = 2.5 - приблизно 8
f2 = fuzz.gaussmf(x, 12, 3) # множина B: дзвін із центром 12 і σ = 3 - приблизно 12


#ЗАВДАННЯ 1: Побудувати трикутну і трапецієподібну функцію приналежності
x1 = np.linspace(0, 20, 201) #вісь x: 201 рівновіддалених точок від 0 до 20
triangle = fuzz.trimf(x1, [3, 8, 17]) #повертає масив значень μ(x) для трикутника
trapeze = fuzz.trapmf(x1, [2, 6, 11, 15]) #повертає масив значень μ(x) для трапеції

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4)) #створює полотно з двома графіками в один ряд
#малює лінію: по осі X точки x1, по Y значення ФН
axes[0].plot(x1, triangle, linewidth=2)
axes[0].set_title("Трикутна ФН (trimf) [3, 8, 17]")
axes[1].plot(x1, trapeze, linewidth=2)
axes[1].set_title("Трапецієподібна ФН (trapmf) [2, 6, 11, 15]")
for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
finish(fig, "1_trimf_trapmf")


#ЗАВДАННЯ 2: Побудувати просту і двостороню функцію приналежності Гауса, утворену за допомогою різних функцій розподілу
x2 = np.linspace(-40, 40, 401)

gauss = fuzz.gaussmf(x2, -6, 5) #простий дзвін: центр у -6 (там значення 1), ширина σ = 5
# склеєний дзвін: ліва половина має центр c1 і ширину σ1, права c2 і σ2
# Якщо c1<c2, між ними виходить плато зі значенням 1
gauss2_a = fuzz.gauss2mf(x2, -20, 3, -8, 5)
gauss2_b = fuzz.gauss2mf(x2, -2, 4, 10, 2)
gauss2_c = fuzz.gauss2mf(x2, 14, 3, 16, 6)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x2, gauss, linewidth=2)
axes[0].set_title("Проста ФП Гауса (gaussmf) [c=-6, σ=5]")
axes[1].plot(x2, gauss2_a, label="[-20, 3, -8, 5]")
axes[1].plot(x2, gauss2_b, label="[-2, 4, 10, 2]")
axes[1].plot(x2, gauss2_c, label="[14, 3, 16, 6]")
axes[1].set_title("Двостороння ФП Гауса (gauss2mf)")
axes[1].legend()
for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
finish(fig, "2_gauss_gauss2")


#ЗАВДАННЯ 3: Побудувати функцію приналежності "узагальнений дзвін"
x3 = np.linspace(0, 20, 401)
#gbellmf(x, a, b, c)
#c - центр, a - половина ширини на рівні 0.5, b - крутизна схилів
#у точках c − a значення μ = 0.5
generalized_bell_1 = fuzz.gbellmf(x3, 4, 3, 10)
generalized_bell_2 = fuzz.gbellmf(x3, 2, 1, 10)
generalized_bell_3 = fuzz.gbellmf(x3, 6, 8, 10)

fig, axes = plt.subplots(figsize=(7, 4))
axes.plot(x3, generalized_bell_1, label="a=4, b=3, c=10")
axes.plot(x3, generalized_bell_2, label="a=2, b=1, c=10")
axes.plot(x3, generalized_bell_3, label="a=6, b=8, c=10")
axes.set_title("ФП \"узагальнений дзвін\" (gbellmf)")
axes.set_xlabel("x")
axes.set_ylabel("μ(x)")
axes.legend()
finish(fig, "3_gbellmf")


#ЗАВДАННЯ 4: Побудувати набір сигмоїдних функцій:
# основну односторонню, яка відкрита зліва чи справа;
# додаткову двосторонню;
# додаткову несиметричну
# b - точка, де μ = 0.5, параметр c - крутизна, знак c визначає бік
# при c > 0 функція росте і відкрита праворуч, інакше спадає і відкрита ліворуч
x4 = np.linspace(0, 20, 401)

#fuzz.sigmf(x, b, c) - основна сигмоїда
# b - центр, потім c - крутизна
sig_right = fuzz.sigmf(x4, 12, 0.7) # відкрита праворуч
sig_left = fuzz.sigmf(x4, 12, -0.7) # відкрита ліворуч
#fuzz.dsigmf(x, b1, c1, b2, c2) - різниця двох сигмоїд
dsig = fuzz.dsigmf(x4, 5, 1.2, 14, 1.2) # двостороння
#fuzz.psigmf(x, b1, c1, b2, c2) - добуток двох сигмоїд
#різна крутизна схилів робить функцію несиметричною
psig = fuzz.psigmf(x4, 6, 0.6, 15, -2) # несиметрична

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(x4, sig_right, label="c = 0.7 (відкрита праворуч)")
axes[0].plot(x4, sig_left, label="c = -0.7 (відкрита ліворуч)")
axes[0].set_title("Основна сигмоїда (sigmf)")
axes[0].legend()
axes[1].plot(x4, dsig, linewidth=2)
axes[1].set_title("Двостороння (dsigmf) [5, 1.2, 14, 1.2]")
axes[2].plot(x4, psig, linewidth=2)
axes[2].set_title("Несиметрична (psigmf) [6, 0.6, 15, -2]")
for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
finish(fig, "4_sigmoid")


#ЗАВДАННЯ 5: Побудувати набір поліноміальних функцій приналежності (Z-, PI- і S-функцій)
x5 = np.linspace(0, 20, 401)

#fuzz.zmf(x, a, b) - Z-функція
# рівна 1 до точки a і плавно спадає до 0 у точці b
z = fuzz.zmf(x5, 6, 13)
# fuzz.pimf(x, a, b, c, d) - PI-функція
#росте від a до b, на відрізку від b до c рівна 1, спадає від c до d
pi = fuzz.pimf(x5, 3, 7, 12, 18)
# fuzz.smf(x, a, b) - S-функція
# 0 до точки a, плавно росте до 1 у точці b і далі рівна 1
s = fuzz.smf(x5, 7, 14)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(x5, z, linewidth=2)
axes[0].set_title("Z-функція (zmf) [6, 13]")
axes[1].plot(x5, pi, linewidth=2)
axes[1].set_title("PI-функція (pimf) [3, 7, 12, 18]")
axes[2].plot(x5, s, linewidth=2)
axes[2].set_title("S-функція (smf) [7, 14]")
for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
finish(fig, "5_zmf_pimf_smf")


#ЗАВДАННЯ 6: Побудувати мінімаксну інтерпретацію логічних операторів
# з використанням операцій пошуку мінімуму і максимуму
#перетин (І, кон'юнкція): μ(x) = min(μA(x), μB(x))
#об'єднання (АБО, диз'юнкція): μ(x) = max(μA(x), μB(x))
and_min = np.fmin(f1, f2) # кон'юнкція (І) = мінімум
or_max = np.fmax(f1, f2) # диз'юнкція (АБО) = максимум

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for ax, res, title in zip(axes, (and_min, or_max),
                          ("Перетин (min) - кон'юнкція", "Об'єднання (max) - диз'юнкція")):
    ax.plot(x, f1, "--", label="A: gaussmf, c=8, σ=2.5")
    ax.plot(x, f2, "--", label="B: gaussmf, c=12, σ=3")
    ax.plot(x, res, "r", linewidth=2.5, label="результат")
    ax.fill_between(x, res, alpha=0.2, color="r")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
    ax.legend()
fig.suptitle("Мінімаксна інтерпретація")
finish(fig, "6_minmax")


#ЗАВДАННЯ 7: Побудувати вірогідну інтерпретацію кон'юнктивну і диз'юнктивних операторів.
# перетин: μ(x) = μA(x) * μB(x), добуток
# об'єднання: μ(x) = μA(x) + μB(x) − μA(x) * μB(x), алгебраїчна сума
and_prob = f1 * f2
or_prob = f1 + f2 - f1 * f2

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for ax, res, title in zip(axes, (and_prob, or_prob),
                          ("Перетин (добуток) - кон'юнкція", "Об'єднання (алгебр. сума) - диз'юнкція")):
    ax.plot(x, f1, "--", label="A: gaussmf, c=8, σ=2.5")
    ax.plot(x, f2, "--", label="B: gaussmf, c=12, σ=3")
    ax.plot(x, res, "r", linewidth=2.5, label="результат")
    ax.fill_between(x, res, alpha=0.2, color="r")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("μ(x)")
    ax.legend()
fig.suptitle("Імовірнісна інтерпретація")
finish(fig, "7_probabilistic")


#ЗАВДАННЯ 8: Побудувати доповнення нечіткої множини, яке описує деяке розмите
# судження і представляє собою математичний опис вербального вираження, який заперечує це нечітка множина.
# доповнення (логічне "НЕ А"): μ(x) = 1 − μA(x)
not_f1 = 1 - f1

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, f1, label="A: gaussmf, c=8, σ=2.5 \"приблизно 8\"")
ax.plot(x, not_f1, "--", linewidth=2, label="НЕ A: \"не приблизно 8\"")
ax.set_title("Доповнення нечіткої множини")
ax.set_xlabel("x")
ax.set_ylabel("μ(x)")
ax.legend()
finish(fig, "8_complement")