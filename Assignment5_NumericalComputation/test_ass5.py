from module_ass5 import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


#a) The values differ by 2.70*10^-18

#b) they differ due to two types of round-off errors
#   Firstly, catastrophic cancellation occurs as the two numbers are very similar
#   causing digits to cancel out, secondly representation round-off error causes
#   the numbers to be rounded to fit the IEE-754 format causing further error.

#c) Method 2 is more accurate, this is because it avoids catastrophic cancellation
#   which occurs when two numbers, similar in magnitude are subtracted.
#   Instead, it works with the differences directly rather than subtracting the
#   squares of the two numbers. This leads to more numerical stability.


# Code for Task 2.4: numerically solving the ODE goes here
#a)
from scipy.integrate import solve_ivp
from module_ass5 import derivative_ode1, exact_solution_ode1
time_span = [0,2]
y_0 = [4]
solution_ODE = solve_ivp(derivative_ode1, time_span, y_0)
print("t values:", solution_ODE.t)
print("y values:", solution_ODE.y[0])

#b)
y_exact = exact_solution_ode1(solution_ODE.t)
print("Exact values:", y_exact)

#c)
import matplotlib.pyplot as plt

#Task 2.4
#c) Plot comparison of exact and numerical solutions

plt.plot(solution_ODE.t, y_exact, 'b-', label='Exact solution')

plt.plot(solution_ODE.t, solution_ODE.y[0], 'ro', label='Numerical solution')

plt.title("Exact vs Numerical Solution")
plt.xlabel("Time t")
plt.ylabel("y(t)")

plt.legend()

plt.savefig("ode1ComparisonPlot.jpg")

plt.show()





# Code and comments for Task 2.6: investigating the MAE goes here
from module_ass5 import mean_absolute_error

y_exact = exact_solution_ode1(solution_ODE.t)
y_approx = solution_ODE.y[0]
MAE_IVP = mean_absolute_error(y_exact, y_approx)
print(f"MAE between numerical and exact solution: {MAE_IVP:.8f}")

#a) The MAE between the numerical and exact solution is 0.00019410

#b) This is a very small error meaning the approximation (numerical solution) is very
#   close to the exact solution, we can observe this on the graph as the red points
#   reside almost on top of the blue line, meaning the numerical solutions are quite accurate.

#c) There are two significant types of round-off errors that may occur
#   Representation error:
#   Certain floating-point numbers cannot be properly represented in binary causing digits to be lost

#   catastrophic cancellation
#   if y_approx and y_exact are similar in magnitude subtraction could
#   result causing the leading digits to be lost and amplify errors overtime






# set Butcher tableau for Euler method
alpha_euler = np.array([1.])
beta_euler = np.array([0.])
gamma_euler = np.array([[0.]])

# Code and comments for Task 3.3 Investigating RK numerical error goes here
import numpy as np


def f(t, y):
    return 2 * np.exp(-5 * t) - 5 * y


def exact_solution(t):
    return (4 + 2 * t) * np.exp(-5 * t)


step_sizes = [0.01, 0.025, 0.05, 0.1, 0.2, 0.25]


y0 = 4
tspan = [0, 2]

e_alpha = np.array([1])
e_beta = np.array([0])
e_gamma = np.array([[0]])

ie_alpha = np.array([0.5, 0.5])
ie_beta = np.array([0, 1])
ie_gamma = np.array([[0, 0],[1, 0]])

rk4_alpha = np.array([1/6, 1/3, 1/3, 1/6])
rk4_beta = np.array([0, 0.5, 0.5, 1])
rk4_gamma = np.array(
    [[0,  0,   0, 0],
    [0.5, 0,   0, 0],
    [0,   0.5, 0, 0],
    [0,   0,   1, 0]])

print("Euler's Method")

for h in step_sizes:

   t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, e_alpha, e_beta, e_gamma)
   t_values = np.array(t_values)

   y_exact_values = exact_solution(t_values)

   mae = mean_absolute_error(y_exact_values, y_numeric)
   print(f"h = {h:.3f}, MAE = {mae:.6e}")


print("Improved Euler Method")
for h in step_sizes:

   t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, ie_alpha, ie_beta, ie_gamma)
   t_values = np.array(t_values)
   y_exact_values = exact_solution(t_values)

   mae = mean_absolute_error(y_exact_values, y_numeric)
   print(f"h = {h:.3f}, MAE = {mae:.6e}")

print("RK4 Method")
for h in step_sizes:
   t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, rk4_alpha, rk4_beta, rk4_gamma)
   t_values = np.array(t_values)
   y_exact_values = exact_solution(t_values)

   mae = mean_absolute_error(y_exact_values, y_numeric)
   print(f"h = {h:.3f}, MAE = {mae:.6e}")






# Code and comments for Task 3.4 Investigating RK stability goes here
import numpy as np
import matplotlib.pyplot as plt


step_sizes = [0.01, 0.025, 0.05, 0.1, 0.2, 0.25]


mae_euler = []
mae_midpoint = []
mae_rk4 = []


for h in step_sizes:
    t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, e_alpha, e_beta, e_gamma)
    t_values = np.array(t_values)
    y_exact = exact_solution(t_values)
    mae = mean_absolute_error(y_exact, y_numeric)
    mae_euler.append(mae)

for h in step_sizes:
    t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, ie_alpha, ie_beta, ie_gamma)
    t_values = np.array(t_values)
    y_exact = exact_solution(t_values)
    mae = mean_absolute_error(y_exact, y_numeric)
    mae_midpoint.append(mae)

for h in step_sizes:
    t_values, y_numeric = explicit_rk_solver(f, tspan, y0, h, rk4_alpha, rk4_beta, rk4_gamma)
    t_values = np.array(t_values)
    y_exact = exact_solution(t_values)
    mae = mean_absolute_error(y_exact, y_numeric)
    mae_rk4.append(mae)


plt.figure()
plt.plot(step_sizes, mae_euler, 'bo-', label='Euler')
plt.plot(step_sizes, mae_midpoint, 'ro-', label='Improved Euler')
plt.plot(step_sizes, mae_rk4, 'go-', label='RK4')

plt.xlabel('Step size (h)')
plt.ylabel('Mean Absolute Error (mae)')
plt.title('Numerical Error in RK Methods')
plt.legend()
plt.grid(True)


plt.savefig("numericalErrorRKmethods.jpg")
plt.show()

#Task 3.4
#b) Observing the graph we see that the Euler's method plot is linear
#   this means that the mean absolute error (mae) is proportional to the step size (h)
#   therefore, we can conclude the global truncation error is O(h)

#c) RK4 is an fourth order method, hence every step (h) is much more accurate than the previous RK methods -
#   this means that less steps (h) are needed to get higher precision results.
#   however, the downside is that RK4 is much more computationally demanding
#   this is because it uses four function evaluations per step compared to
#   Euler's method and the Improved Euler method which just use 1 and 2 function evaluations respectively


#Task 3.5
# Euler Method
t_euler, y_euler = explicit_rk_solver(f, tspan, y0, h, e_alpha, e_beta, e_gamma)
t_euler = np.array(t_euler)
y_exact_euler = exact_solution(t_euler)

# Improved Euler Method
t_mid, y_mid = explicit_rk_solver(f, tspan, y0, h, ie_alpha, ie_beta, ie_gamma)
t_mid = np.array(t_mid)
y_exact_mid = exact_solution(t_mid)

# RK4 Method
t_rk4, y_rk4 = explicit_rk_solver(f, tspan, y0, h, rk4_alpha, rk4_beta, rk4_gamma)
t_rk4 = np.array(t_rk4)
y_exact_rk4 = exact_solution(t_rk4)


plt.figure()

plt.plot(t_euler, y_euler, 'b-o', label='Euler')
plt.plot(t_mid, y_mid, 'r--o', label='Improved Euler')
plt.plot(t_rk4, y_rk4, 'g-.o', label='RK4')
plt.plot(t_rk4, y_exact_rk4, 'k-', label='Exact Solution')  # Overlay

plt.xlabel("Time t")
plt.ylabel("y(t)")
plt.title("Stability of RK Methods at h = 0.5")
plt.legend()
plt.grid(True)

plt.savefig("stabilityRKmethods.jpg")
plt.show()

#Task 3.5
#b) From observing the graph we can see that Euler's method is numerically unstable at h = 0.5
#   as it rapidly deviates far from the exact solution curve.
#   The improved Euler method is better, but still demonstrates noticeable error and does not
#   follow the exact solution curve, finally the RK4 method provides the best numerical approximation
#   for the exact solution and lies very close to the exact solution curve.

#c) To assess the numerical stability in the absence of a known mathematical condition
# we can compare the numerical solution to the exact solution,
# metrics such as large deviations or error spikes when we increase the step size
# indicates an unstable numerical solution, if the numerical solution
# consistently remains distant from the exact solution
# or gives vague, non-accurate estimate then this is also an indicator of numerical instability.
