"""Логические векторы по вещественной матрице (вариант 7)."""


def zero_columns(matrix):
    """Для каждого столбца: True, если все его элементы нулевые."""
    if not matrix:
        return []
    return [all(row[k] == 0 for row in matrix) for k in range(len(matrix[0]))]


def descending_rows(matrix):
    """Для каждой строки: True, если элементы упорядочены по убыванию."""
    return [all(row[j] >= row[j + 1] for j in range(len(row) - 1))
            for row in matrix]


def symmetric_rows(matrix):
    """Для каждой строки: True, если строка симметрична."""
    return [row == row[::-1] for row in matrix]
