from collections import defaultdict, OrderedDict
from pprint import pprint

import matplotlib.pyplot as plt
from sympy import Integer as spInt

correct_cube = {i: spInt(1) / spInt(6) for i in range(1, 6 + 1)}
incorrect_cube = {i: spInt(1) / spInt(12) for i in range(1, 6 + 1)}
incorrect_cube[3] = incorrect_cube[4] = spInt(1) / spInt(3)

theta = lambda psi, mu: psi ** mu - mu ** psi


def probability(table, value):
    return table[value]


def find_theta(theta_func, psi_table, mu_table):
    theta_table = defaultdict(int)
    for psi in psi_table:
        for mu in mu_table:
            theta = theta_func(psi, mu)
            theta_probablity = probability(psi_table, psi) * probability(mu_table, mu)
            theta_table[theta] += theta_probablity
    return theta_table


def find_expectation(table):
    return sum(value * probability(table, value) for value in table)


def find_dispersion(table, expectation):
    return sum(probability(table, value) * ((value - expectation) ** 2) for value in table)


def prefix_sum(table, stop_value):
    sum = 0
    for event in table:
        sum += probability(table, event)
        if event == stop_value:
            return sum


theta_table = find_theta(theta, correct_cube, incorrect_cube)
pprint(theta_table)
expectation = find_expectation(theta_table)
dispersion = find_dispersion(theta_table, expectation)
print(f"E={expectation}")
print(f"D={dispersion}")

od = OrderedDict(sorted(theta_table.items()))

poss = []
x_axis = []
for ev in od:
    x_axis.append(ev)
    poss.append(prefix_sum(od, ev))

plt.figure()
plt.xlabel("Событие")
plt.ylabel("Вероятность")
plt.scatter(x_axis, poss)
plt.grid(True)
# plt.savefig("dependency_chart.png")

plt.show()
