import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Визначення функції та межі інтегрування
def f(x):
    return np.sin(x)

a = 0          # Нижня межа
b = np.pi      # Верхня межа

# Метод Монте-Карло
N = 100_000
np.random.seed(42)

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, 1, N)          # sin(x) на [0, π] лежить у [0, 1]

# Точки, що потрапили під криву
under_curve = y_random <= f(x_random)
monte_carlo_result = (b - a) * 1 * np.sum(under_curve) / N   # (b-a) * h_max * частка

# Аналітичний результат: ∫sin(x)dx від 0 до π = [-cos(x)] = -cos(π) + cos(0) = 2 ---
analytical_result = 2.0

# scipy.integrate.quad
quad_result, quad_error = integrate.quad(f, a, b)

# Результати
print("=" * 45)
print(f"{'Метод':<25} {'Результат':>10} {'Похибка':>10}")
print("-" * 45)
print(f"{'Монте-Карло':<25} {monte_carlo_result:>10.6f} {abs(monte_carlo_result - analytical_result):>10.6f}")
print(f"{'scipy quad':<25} {quad_result:>10.6f} {abs(quad_result - analytical_result):>10.6f}")
print(f"{'Аналітично':<25} {analytical_result:>10.6f} {'—':>10}")
print("=" * 45)
print(f"\nВисновок: метод Монте-Карло дав похибку "
      f"{abs(monte_carlo_result - analytical_result):.10f} "
      f"при N={N:,} точок.")

# Графік
x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2, label='f(x) = sin(x)')

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label=f'Площа (MC) ≈ {monte_carlo_result:.4f}')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([-0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від 0 до π')
ax.legend()
plt.grid()
plt.show()
