from matrix_vectors import descending_rows, symmetric_rows, zero_columns


def test_zero_columns():
    m = [[0.0, 1.0, 2.0], [0.0, 3.0, 4.0], [0.0, 5.0, 6.0]]
    assert zero_columns(m) == [True, False, False]


def test_descending_rows():
    m = [[6.0, 7.0, 9.0], [0.0, 0.0, 0.0], [9.0, 8.0, 1.0]]
    assert descending_rows(m) == [False, True, True]


def test_symmetric_rows():
    m = [[8.0, 9.0, 8.0], [1.0, 2.0, 3.0]]
    assert symmetric_rows(m) == [True, False]


def test_all_zero_matrix():
    m = [[0.0, 0.0], [0.0, 0.0]]
    assert zero_columns(m) == [True, True]
    assert descending_rows(m) == [True, True]
    assert symmetric_rows(m) == [True, True]
