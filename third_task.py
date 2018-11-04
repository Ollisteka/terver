from math import sqrt

from sympy import Integer as spInt

from first_task import RandomValuesDescriber


def find_dispersion(probability, expectation):
    return sum(probability[value] * ((value - expectation) ** 2) for value in probability)


def find_expectation(probability):
    return sum(value * probability[value] for value in probability)


def find_covariance_and_correlation(theta, xi, nu):
    describer = RandomValuesDescriber(theta, xi, nu)
    # describer.print_distribution_law()
    covariance = describer.expectation
    xi_d = find_dispersion(xi, find_expectation(xi))
    nu_d = find_dispersion(nu, find_expectation(nu))
    correlation = covariance / sqrt(xi_d * nu_d)
    return covariance, correlation


if __name__ == "__main__":
    correct_cube = {i: spInt(1) / spInt(6) for i in range(1, 6 + 1)}
    xi = {
        0: spInt(1) / spInt(3),
        1: spInt(1) / spInt(2),
        -1: spInt(1) / spInt(6),
    }

    xi_2 = {
        0: spInt(1) / spInt(3),
        1: spInt(2) / spInt(3),
    }
    my_theta = lambda x, y: (x - (spInt(1) / spInt(3))) * (x ** 2 - (spInt(2) / spInt(3)))
    covariance, correlation = find_covariance_and_correlation(my_theta, xi, xi_2)
    print(f"covariance={covariance}")
    print(f"correlation={correlation}")

    xi = {
        -2: spInt(1) / spInt(4),
        -1: spInt(1) / spInt(4),
        1: spInt(1) / spInt(4),
        2: spInt(1) / spInt(4),
    }

    xi_2 = {
        2: spInt(1) / spInt(2),
        4: spInt(1) / spInt(2),
    }
    my_theta = lambda x, y: x * (x ** 2 - 3)
    covariance, correlation = find_covariance_and_correlation(my_theta, xi, xi_2)
    print(f"covariance={covariance}")
    print(f"correlation={correlation}")
