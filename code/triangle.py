import matplotlib.pyplot as plt
import numpy as np

# Функция для нахождения точки на отрезке между двумя точками
def point_on_line(P1, P2, t):
    return P1 + t * (P2 - P1)


def draw_triangle_with_custom_lines(n_left, n_right):
    # Определяем вершины треугольника
    A = np.array([0, 0])  # нижний левый угол
    B = np.array([1, 0])  # нижний правый угол
    C = np.array([0.5, 1])  # верхняя вершина

    # Вычисляем точки на сторонах:
    # Для вершины A (нижний левый) — линии идут к стороне BC
    t_values_A = [i / (n_left + 1) for i in range(1, n_left + 1)]
    points_A = [point_on_line(B, C, t) for t in t_values_A]

    # Для вершины B (нижний правый) — линии идут к стороне AC
    t_values_B = [i / (n_right + 1) for i in range(1, n_right + 1)]
    points_B = [point_on_line(A, C, t) for t in t_values_B]

    # Настройка графика
    plt.figure(figsize=(6, 6))
    plt.axis("equal")

    # Рисуем границы треугольника
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    plt.plot(triangle_x, triangle_y, "k-", lw=2, label="Границы треугольника")

    # Рисуем линии из вершины A (нижний левый)
    for idx, P in enumerate(points_A):
        plt.plot(
            [A[0], P[0]],
            [A[1], P[1]],
            "b--",
            lw=2,
            label="Линии из A" if idx == 0 else "",
        )

    # Рисуем линии из вершины B (нижний правый)
    for idx, P in enumerate(points_B):
        plt.plot(
            [B[0], P[0]],
            [B[1], P[1]],
            "r--",
            lw=2,
            label="Линии из B" if idx == 0 else "",
        )

    # Подписываем вершины
    plt.text(A[0] - 0.05, A[1] - 0.05, "A", fontsize=12, color="k")
    plt.text(B[0] + 0.02, B[1] - 0.05, "B", fontsize=12, color="k")
    plt.text(C[0] - 0.03, C[1] + 0.02, "C", fontsize=12, color="k")

    plt.legend(loc="upper right")
    plt.title(f"Треугольник с {n_left} линиями из A и {n_right} из B")
    plt.show()


# Пример вызова функции с разным количеством линий
draw_triangle_with_custom_lines(n_left=3, n_right=5)


def count_quadrilaterals(L, R):
    """Функция для подсчёта количества четырёхугольников в треугольнике"""
    if L < 1 or R < 1:
        return 0
    return (L * R * (L + 1) * (R + 1)) // 4


if __name__ == "__main__":
    # Пример использования функции
    L = 3  # Количество точек по оси X
    R = 2  # Количество точек по оси Y
    result = count_quadrilaterals(L, R)
    print(f"Количество четырёхугольников в треугольнике: {result}")

    # Пример вызова функции с разным количеством линий
    draw_triangle_with_custom_lines(n_left=L, n_right=R)
