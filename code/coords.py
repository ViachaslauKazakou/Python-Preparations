
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from matplotlib.patches import Polygon as mplPolygon, Circle

def main():
    try:
        # Ввод координат центра круга и диаметра
        x_circle = float(input("Введите координату X центра круга: "))
        y_circle = float(input("Введите координату Y центра круга: "))
        diameter = float(input("Введите диаметр круга: "))
        radius = diameter / 2

        # Ввод координат противоположных вершин прямоугольника
        x1 = float(input("Введите X1 первой вершины прямоугольника: "))
        y1 = float(input("Введите Y1 первой вершины прямоугольника: "))
        x2 = float(input("Введите X2 противоположной вершины прямоугольника: "))
        y2 = float(input("Введите Y2 противоположной вершины прямоугольника: "))

        # Ввод координат точки для проверки
        x_point = float(input("Введите координату X точки для проверки: "))
        y_point = float(input("Введите координату Y точки для проверки: "))
        point = Point(x_point, y_point)

        # Построение графика с кругом и прямоугольником
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.axhline(0, color='gray', linestyle='--')
        plt.axvline(0, color='gray', linestyle='--')

        # Добавление круга
        circle = Circle((x_circle, y_circle), radius=radius, color='blue', fill=False, linewidth=2)
        ax.add_patch(circle)

        # Добавление прямоугольника
        rect_x1, rect_x2 = min(x1, x2), max(x1, x2)
        rect_y1, rect_y2 = min(y1, y2), max(y1, y2)
        rect_points = [(rect_x1, rect_y1), (rect_x1, rect_y2), (rect_x2, rect_y2), (rect_x2, rect_y1)]
        rectangle = mplPolygon(rect_points, edgecolor='red', fill=False, linewidth=2)
        ax.add_patch(rectangle)

        # Вычисление пересечения с помощью Shapely
        circle_shape = Point(x_circle, y_circle).buffer(radius)  # Круг как геометрическая фигура
        rect_shape = Polygon(rect_points)  # Прямоугольник как полигон
        intersection = circle_shape.intersection(rect_shape)

        # Отрисовка пересекающейся области
        if not intersection.is_empty:
            x_inter, y_inter = intersection.exterior.xy
            plt.fill(x_inter, y_inter, color='purple', alpha=0.5, label="Пересечение")

        # Проверка, попадает ли точка в пересекающуюся область
        if intersection.contains(point):
            print(f"Точка ({x_point}, {y_point}) находится внутри пересекающейся области.")
            plt.scatter(x_point, y_point, color='green', label=f"Точка внутри ({x_point}, {y_point})")
            plt.text(x_point, y_point, f'  ({x_point}, {y_point})', fontsize=12, color='blue')
        else:
            print(f"Точка ({x_point}, {y_point}) не попадает в пересекающуюся область.")
            plt.scatter(x_point, y_point, color='orange', label=f"Точка вне области ({x_point}, {y_point})")
            plt.text(x_point, y_point, f'  ({x_point}, {y_point})', fontsize=12, color='blue')

        # Настройка графика
        plt.title("Пересечение круга и прямоугольника с точкой")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        ax.set_xlim(min(rect_x1, x_circle - radius, x_point) - 1, max(rect_x2, x_circle + radius, x_point) + 1)
        ax.set_ylim(min(rect_y1, y_circle - radius, y_point) - 1, max(rect_y2, y_circle + radius, y_point) + 1)

        plt.show()

    except ValueError:
        print("Ошибка: Введите числовые значения.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
