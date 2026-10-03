"""Консольный ввод матрицы и вывод логических векторов."""
from matrix_vectors import descending_rows, symmetric_rows, zero_columns


def read_matrix():
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    print("Введите элементы матрицы по строкам:")
    matrix = []
    for i in range(n):
        row = list(map(float, input("Строка {}: ".format(i + 1)).split()))
        if len(row) != m:
            raise ValueError("В строке должно быть {} элементов".format(m))
        matrix.append(row)
    return matrix


def main():
    matrix = read_matrix()
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    print("\nРезультаты анализа:")
    print("1. Нулевые столбцы:", zero_columns(matrix))
    print("2. Строки по убыванию:", descending_rows(matrix))
    print("3. Симметричные строки:", symmetric_rows(matrix))


if __name__ == "__main__":
    main()
