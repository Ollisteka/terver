from sympy import Integer as spInt

from first_task import RandomValuesDescriber

correct_cube = {i: spInt(1) / spInt(6) for i in range(1, 6 + 1)}
incorrect_cube = {i: spInt(1) / spInt(12) for i in range(1, 6 + 1)}
incorrect_cube[3] = incorrect_cube[4] = spInt(1) / spInt(3)

my_theta = lambda xi, mu: xi ** mu - mu ** xi
their_theta = lambda xi, mu: min(2 ** xi, mu)

my_describer = RandomValuesDescriber(my_theta, correct_cube, incorrect_cube)
their_describer = RandomValuesDescriber(their_theta, correct_cube, incorrect_cube)

my_exp = my_describer.expectation
their_exp = their_describer.expectation

covariance_theta = lambda xi, mu: (my_theta(xi, mu) - my_exp) * (their_theta(xi, mu) - their_exp)
final_describer = RandomValuesDescriber(covariance_theta, correct_cube, incorrect_cube)

covariance = final_describer.expectation
correlation = covariance / (my_describer.standard_deviation * their_describer.standard_deviation)

print(f"Cov(xi ** mu - mu ** xi, min(2**xi, mu)) = {covariance}")
print(f"Correlation of xi ** mu - mu ** xi and min(2**xi, mu) = {correlation}")
