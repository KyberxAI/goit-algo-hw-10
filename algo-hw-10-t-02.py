import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return np.sin(x)


def monte_carlo_integral(func, x1, x2, y1, y2, n):

    # Генерація випадкових точок
    points = [(random.uniform(x1, x2), random.uniform(y1, y2))
              for _ in range(n)]

    # Підрахунок точок над і під віссю X
    positive_points = 0
    negative_points = 0

    for x, y in points:
        if 0 <= y <= func(x):
            positive_points += 1
        elif func(x) <= y < 0:
            negative_points += 1

    # Площа прямокутника генерації випадкових точок
    rectangle_area = (x2 - x1) * (y2 - y1)

    # Оцінка площ під графіком функції
    positive_area = positive_points / n * rectangle_area
    negative_area = negative_points / n * rectangle_area

    # Визначений інтеграл з урахуванням знака
    integral = positive_area - negative_area

    print(f"Кількість точок             : {n}")
    print(f"  Точок у додатній області    : {positive_points}")
    print(f"  Точок у від'ємній област    : {negative_points}")
    print(f"    Площа у додатній області    : {positive_area}")
    print(f"    Площа у від'ємній області   : {negative_area}")
    print(f"\nІнтеграл методом Монте-Карло    : {integral:.10f}\n")


# Межі інтегрування та прямокутника
x1 = -np.pi/2
x2 = np.pi
y1 = -1
y2 = 1

print(f"\nОбчислюємо інтеграл f(x) = sin(x) "
      f"\nвід {x1} до {x2} \n")

# Обчислення через scipy
result, error = quad(f, x1, x2)
print(f"Результат quad: {result:.10f}")
print(f"Оцінка похибки quad: {error:.2e}\n")

# Метод Монте-Карло
print(f"Обчислення інтеграла через площу методом Монте-Карло \n")

monte_carlo_integral(f, x1, x2, y1, y2, 1000)
monte_carlo_integral(f, x1, x2, y1, y2, 8000)
monte_carlo_integral(f, x1, x2, y1, y2, 32000)
monte_carlo_integral(f, x1, x2, y1, y2, 128000)
monte_carlo_integral(f, x1, x2, y1, y2, 512000)

# ========== Графік функції sin(x) ==========


x = np.linspace(x1, x2, 200)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'purple', linewidth=2, label='$f(x) = \\sin x$')
plt.fill_between(x, 0, y, alpha=0.3, color='purple')
plt.axvline(x=x1, color='red', linestyle='--', linewidth=1)
plt.axvline(x=x2, color='red', linestyle='--', linewidth=1)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.title('$\\int_{x1}^{x2} \\sin x \\, dx $', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.show()
