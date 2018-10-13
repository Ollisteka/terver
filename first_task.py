from collections import defaultdict, OrderedDict

import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sympy import Integer as spInt


class RandomValuesDescriber:
    def __init__(self, theta_func, psi, mu):
        self.psi = psi
        self.mu = mu
        self.theta_table = defaultdict(int)
        self.find_theta(theta_func)
        self.expectation = 0
        self.find_expectation()
        self.dispersion = 0
        self.find_dispersion()

    def probability(self, table, value):
        return table[value]

    def find_theta(self, theta_func):
        for psi in self.psi:
            for mu in self.mu:
                theta = theta_func(psi, mu)
                theta_probablity = self.probability(self.psi, psi) * self.probability(self.mu, mu)
                self.theta_table[theta] += theta_probablity

    def find_expectation(self):
        self.expectation = sum(value * self.probability(self.theta_table, value) for value in self.theta_table)

    def find_dispersion(self):
        self.dispersion = sum(self.probability(self.theta_table, value) * ((value - self.expectation) ** 2)
                              for value in self.theta_table)

    def prefix_sum(self, table, stop_value):
        sum = 0
        for event in table:
            sum += self.probability(table, event)
            if event == stop_value:
                return sum

    def show_plot(self):
        ordered_events = OrderedDict(sorted(self.theta_table.items()))
        prefix_sums = []
        events = list(ordered_events.keys())
        for ev in events:
            prefix_sums.append(self.prefix_sum(ordered_events, ev))

        plt.figure()
        plt.xlabel("Событие")
        plt.ylabel("Вероятность")
        plt.scatter(events, prefix_sums, c='r', marker='*')  # разбросали точки

        min_event = events[0]
        plt.arrow(min_event, 0, -1000, 0)
        data = []
        for i in range(len(ordered_events) - 1):
            #             [(x1,x2),(y1,y2), цвет]
            data.extend([(events[i], events[i + 1]), (prefix_sums[i + 1], prefix_sums[i + 1]), 'b'])
        plt.plot(*data)  # проведём линии
        plt.grid(True)
        plt.show()

    def print_distribution_law(self):
        print("Закон распределения:")
        ordered_events = OrderedDict(sorted(self.theta_table.items()))
        x = PrettyTable()
        x.field_names = ["Событие", "Вероятность"]
        for item in ordered_events.items():
            x.add_row(item)

        print(x)


correct_cube = {i: spInt(1) / spInt(6) for i in range(1, 6 + 1)}
incorrect_cube = {i: spInt(1) / spInt(12) for i in range(1, 6 + 1)}
incorrect_cube[3] = incorrect_cube[4] = spInt(1) / spInt(3)

theta = lambda psi, mu: psi ** mu - mu ** psi

describer = RandomValuesDescriber(theta, correct_cube, incorrect_cube)
describer.print_distribution_law()
print(f"E={describer.expectation}")
print(f"D={describer.dispersion}")
describer.show_plot()
