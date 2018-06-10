def linear_regression(x, y):

    cov_matrix = np.cov(x, y)
    a = cov_matrix[0, 1] / cov_matrix[0, 0]
    b = np.mean(y) - a * np.mean(x)

    return a, b
