import math
import tkinter as tk
from tkinter import messagebox
import unittest

entry = None  # Объявляем entry в глобальной области видимости

def transform_value(x):

    # Функция для преобразования значения x в соответствии с заданными условиями.

    if x < 1.5:
        y = math.sin(x) * math.sqrt(x)
    else:
        y = math.exp(1.4 * x ** 2) - 4.9
    return y

class TransformationTestCase(unittest.TestCase):
    def test_transform_value(self):
        # Тестирование преобразования для значений x < 1.5
        x = 1.0
        expected_y = math.sin(x) * math.sqrt(x)
        self.assertAlmostEqual(transform_value(x), expected_y, places=4)

        # Тестирование преобразования для значений x >= 1.5
        x = 2.0
        expected_y = math.exp(1.4 * x ** 2) - 4.9
        self.assertAlmostEqual(transform_value(x), expected_y, places=4)


def main():
    try:
        x = float(input("Введите значение x: "))
        result = transform_value(x)
        print("Результат преобразования:", result)
    except ValueError:
        print("Ошибка: Введите числовое значение для x.")

def calculate():
    global entry  # Используем глобальную переменную entry
    try:
        x = float(entry.get())
        result = transform_value(x)
        messagebox.showinfo("Результат", f"Результат преобразования: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение для x.")

def create_gui():
    global entry  # Используем глобальную переменную entry
    window = tk.Tk()
    window.title("Программа для вычисления значения")
    window.geometry("300x150")

    label = tk.Label(window, text="Введите значение x:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Вычислить", command=calculate)
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    # Запуск тестов
    unittest.main(argv=[''], exit=False)

    # Запуск ввода значения x и вычисления через командную строку
    # main()

    # Запуск графического интерфейса пользователя
    create_gui()
