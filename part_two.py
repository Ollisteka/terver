from math import sqrt

from sympy import Integer as spInt

from first_task import RandomValuesDescriber

correct_cube = {i: spInt(1) / spInt(6) for i in range(1, 6 + 1)}
incorrect_cube = {i: spInt(1) / spInt(12) for i in range(1, 6 + 1)}
incorrect_cube[3] = incorrect_cube[4] = spInt(1) / spInt(3)

my_theta = lambda psi, mu: psi ** mu - mu ** psi
their_theta = lambda psi, mu: min(2 ** psi, mu)

my_describer = RandomValuesDescriber(my_theta, correct_cube, incorrect_cube)
their_describer = RandomValuesDescriber(their_theta, correct_cube, incorrect_cube)

my_theta = my_describer.theta_table
their_theta = their_describer.theta_table

my_exp = my_describer.expectation
their_exp = their_describer.expectation

my_disp = my_describer.dispersion
their_disp = their_describer.dispersion

covariance_theta = lambda x, y: (x - my_exp) * (y - their_exp)
final_describer = RandomValuesDescriber(covariance_theta, my_theta, their_theta)

covariance = final_describer.expectation
correlation = covariance / sqrt(my_disp * their_disp)

print(f"Cov(psi ** mu - mu ** psi, min(2**psi, mu)) = {covariance}")
print(f"Correlation of psi ** mu - mu ** psi and min(2**psi, mu) = {correlation}")
