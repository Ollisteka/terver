from collections import defaultdict, OrderedDict
from math import sqrt, log

from prettytable import PrettyTable
from sympy import Integer as spInt

from third_task import find_expectation, find_dispersion


def print_distribution_law(t, name=""):
    print(f"Закон распределения {name}:")
    ordered_events = OrderedDict(sorted(t.items()))
    x = PrettyTable()
    x.field_names = ["Событие", "Вероятность"]
    for item in ordered_events.items():
        x.add_row(item)

    print(x)


def get_information_total(probability):
    return -log(sum(probability[value] for value in probability))


def get_information(probability_value):
    return -log(probability_value)


def get_conditional_entropy(table, xi_table):
    outer_sum = 0
    for i in range(3):
        inner_sum = 0
        xi_i = xi_table[i + 1]
        for j in range(3):
            prob = table[j][i] / xi_i
            inner_sum += prob * log(prob)
        outer_sum += xi_i * (-inner_sum)
    return outer_sum


if __name__ == "__main__":
    xi = [1, 2, 3]
    nu = [1, 2, 3]

    table = [[spInt(3) / spInt(24), spInt(2) / spInt(24), spInt(5) / spInt(24)],
             [spInt(2) / spInt(24), spInt(2) / spInt(24), spInt(3) / spInt(24)],
             [spInt(3) / spInt(24), spInt(2) / spInt(24), spInt(2) / spInt(24)]]

    for row in table:
        row.append(sum(row))

    table.append([0, 0, 0, 0])

    for i in range(3):
        table[3][i] = sum(table[j][i] for j in range(0, 3))

    x = PrettyTable()
    # x.field_names = ["Событие", "Вероятность"]
    for row in table:
        x.add_row(row)

    print(x)

    xi_table = {xi[i]: table[3][i] for i in range(3)}
    nu_table = {nu[i]: table[i][3] for i in range(3)}

    xi_exp = find_expectation(xi_table)
    nu_exp = find_expectation(nu_table)

    xi_mul_nu = defaultdict(int)
    for xi_val in range(3):
        for nu_val in range(3):
            xi_mul_nu[(xi_val + 1) * (nu_val + 1)] += table[xi_val][nu_val]

    print_distribution_law(xi_mul_nu, "xi*nu")
    xi_mul_nu_exp = find_expectation(xi_mul_nu)
    covariance = xi_mul_nu_exp - xi_exp * nu_exp
    xi_d = find_dispersion(xi_table, xi_exp)
    nu_d = find_dispersion(nu_table, nu_exp)
    correlation = covariance / sqrt(xi_d * nu_d)

    print(f"E(xi)={xi_exp}")
    print(f"E(nu)={nu_exp}")
    print(f"E(xi*mu)={xi_mul_nu_exp}")
    print(f"D(xi)={xi_d}")
    print(f"D(nu)={nu_d}")
    print(f"a) covariance={covariance}")
    print(f"b) correlation={correlation}")
    print(f"c) I((ξ; η) = (2; 3))={get_information(table[2][1])}")

    union_entropy = -sum(sum(table[i][j] * log(table[i][j]) for j in range(3)) for i in range(3))
    print(f"d) H(xi, nu)={union_entropy}")
    h_xi = -sum(xi_table[i + 1] * log(xi_table[i + 1]) for i in range(3))
    print(f"H(xi) lect={h_xi}")
    conditional_entropy = union_entropy - h_xi
    print(f"e) H(nu|xi) lect={conditional_entropy}")

    conditional_entropy = get_conditional_entropy(table, xi_table)
    print(f"e) H(nu|xi)={conditional_entropy}")
    # print_distribution_law(xi_table)
    # print_distribution_law(nu_table)
