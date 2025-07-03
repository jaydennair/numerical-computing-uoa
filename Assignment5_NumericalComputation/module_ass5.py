# import statements
import numpy as np


def difference_squares(x, y):
    """
    Computes and prints the difference of squares using the following methods:
    Method 1: z1 = x^2 - y^2
    Method 2: z2 = (x - y)(x + y)
    Both values are printed to 32dp
    """
    z1 = x ** 2 - y ** 2
    z2 = (x - y) * (x + y)
    print(f"z1 = {z1:.32f}")
    print(f"z2 = {z2:.32f}")
    return z1, z2

z1, z2 = difference_squares(1 + 2 ** -29, 1 + 2 ** -30)
abs_error = abs(z1 - z2)
print(f"abs_error = {abs_error:.32f}")
#task 1.2
#a) The values differ by 2.70*10^-18

#b) they differ due to two types of round-off errors
#   Firstly, catastrophic cancellation occurs as the two numbers are very similar
#   causing digits to cancel out, secondly representation round-off error causes
#   the numbers to be rounded to fit the IEE-754 format causing further error.

#c) Method 2 is more accurate, this is because it avoids catastrophic cancellation
#   which occurs when two numbers, similar in magnitude are subtracted.
#   Instead, it works with the differences directly rather than subtracting the
#   squares of the two numbers. This leads to more numerical stability.




def relative_error_subtraction(x,y,z_exact):
    """
    calculates and displays the difference of two floating point numbers,
    the difference will be compared to the exact value
    - x, y, z_approx, z_exact (64dp)
    - relative error (16dp)
    """
    approx_z = x - y
    error_relative = abs(z_exact - approx_z) / abs(z_exact)

    print(f"The value of x to 64dp is:\n{x:.64f}")
    print(f"The value of y to 64dp is:\n{y:.64f}")
    print(f"The approximate value of z to 64dp is:\n{approx_z:.64f}")
    print(f"The exact value of z to 64dp is:\n{z_exact:.64f}")
    print(f"The relative error to 16dp is: {error_relative:.16f}")
relative_error_subtraction(1 + 1e-15, 1 + 2e-15, -1e-15)
#task 1.4
#a) the relative error is 0.1118215802998748

#b) The relative error is caused by catastrophic cancellation as two numbers
#   of very similar magnitude are subtracted causing significant digits to cancel out
#   this will also cause any existing round-off errors to amplify



def exact_solution_ode1(t):
    """
    Computes the exact solution to the ODE dy/dt + 5y = 2e^(-5t), y(0) = 4,
    at time t (float or NumPy array).

    Parameters:
    t (float or np.ndarray): Time value(s)

    Returns:
    y_exact (float or np.ndarray): The exact value(s) of y at time t
     """
    yc = 4 * np.exp(-5 * t)
    yp = 2 * t * np.exp(-5 * t)
    y_exact = yc + yp
    return y_exact



def mean_absolute_error(y_exact, y_approx):
    """
    Computes the mean absolute error between two arrays
    (excluding the initial value) containing exact values and approximated values.


    Parameters:
    y_exact (np.ndarray): The exact solution values.
    y_approx (np.ndarray): The numerical approximation values.

    Returns:
    float: The mean absolute error.
    """
    total_error = 0
    for i in range(len(y_exact)):
        total_error += abs(y_exact[i] - y_approx[i])
    mae = total_error / (len(y_exact) - 1)
    return mae

yx = np.array([0, 0.4, 1])
ya = np.array([0, 0.5, 0.9])
mae = mean_absolute_error(yx, ya)
print(f"mae is: {mae:.4f}")





def derivative_ode1(t, y):
        """
        Calculates the dy/dt term for ODE (7)

        Parameters:
        t (float): Time value
        y (float): Value of y at time t

        Returns:
        float: The value of dy/dt at time t
        """
        dydt = 2 * np.exp(-5 * t) - 5 * y
        return dydt




def euler_step(f, t, y, h):
    """
    Calculate one step of the Euler method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    y_new = y + h * f0
    return y_new


def improved_euler_step(f, t, y, h):
    """
    Calculate one step of the Improved Euler method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    f1 = f(t + h, y + h * f0)
    y_new = y + h * 0.5 * (f0 + f1)
    return y_new


def classic_rk4_step(f, t, y, h):
    """
    Calculate one step of the Classic RK4 method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    f1 = f(t + h * 0.5, y + h * 0.5 * f0)
    f2 = f(t + h * 0.5, y + h * 0.5 * f1)
    f3 = f(t + h, y + h * f2)
    y_new = y + h * (f0 + 2. * f1 + 2. * f2 + f3) / 6.
    return y_new


def explicit_rk_step(f, t, y, h, alpha, beta, gamma):
    """
       Performs the Runge-Kutta method using a given Butcher tableau for a single step size

       Parameters:
       f (function): The function describing the ODE, with form f(t, y).
       t (float): current time
       y (float): current value y(t).
       h (float): The step size for the RK method.
       alpha (list of float): The weightings used to combine the stage slopes in the final step
       beta (list of float): the weightings used to describe the time point for each RK stage
       gamma (list of list of float): The LT matrix relating the previous stage
       to the next stage slope.

       Returns:
       float: The estimated value of y at time t + h.
    """
    s = len(alpha)
    slopes = []

    for i in range(s):
        intermediate_y = y
        for j in range(i):
            intermediate_y += h * gamma[i][j] * slopes[j]

        t_stage = t + beta[i] * h
        slope_i = f(t_stage, intermediate_y)
        slopes.append(slope_i)

    y_new = y
    for i in range(s):
        y_new += h * alpha[i] * slopes[i]

    return y_new



def explicit_rk_solver(f, tspan, y0, h, alpha, beta, gamma):
    """
    Solves an ODE using an explicit Runge-Kutta method over a fixed time interval.

    Parameters:
    f (function): The function defining the ODE, of the form f(t, y).
    tspan (list or tuple): A list with 2 elements stating the time interval.
    y0 (float): The initial condition y(t_start).
    h (float): The step size.
    alpha (list of float): The weightings used to combine the stage slopes in the final step
    beta (list of float): the weightings used to describe the time point for each RK stage
    gamma (list of list of float): The LT matrix relating the previous stage

    Returns:
    Two lists:
    - t_values: list of time points (including t_start and t_end)
    - y_values: list of solution values y at each time point
    """

    import numpy as np

    t_start, t_end = tspan
    n = int((t_end - t_start) / h)

    t_values = [t_start]
    y_values = [y0]

    current_t = t_start
    current_y = y0

    for i in range(1, n+1):
        y_next = explicit_rk_step(f, current_t, current_y, h, alpha, beta, gamma)
        current_t += h
        t_values.append(current_t)
        y_values.append(y_next)
        current_y = y_next
    return t_values, y_values

