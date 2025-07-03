import numpy as np
import matplotlib.pyplot as plt
#Author: Jayden Krish Nair

#Task 1.1
def vandermonde3(ti, yi):
    """
    Constructs a 3x3 Vandermonde matrix and RHS vector for quadratic regression,
    using a set of measurement points and values

    Parameters:
    ti (array): Measurement points
    yi (array): Measurement values

    Returns:
    A (array): 3x3 Vandermonde matrix
    b (array): RHS vector
    """
    sum_yi = 0
    sum_ty = 0
    sum_t2y = 0

    sum_t0 = len(ti)
    sum_t1 = 0
    sum_t2 = 0
    sum_t3 = 0
    sum_t4 = 0

    for i in range(len(ti)):


        sum_ty += ti[i] * yi[i]
        sum_yi += yi[i]
        sum_t2y += ti[i] ** 2 * yi[i]

        sum_t1 += ti[i]
        sum_t2 += ti[i] ** 2
        sum_t3 += ti[i] ** 3
        sum_t4 += ti[i] ** 4

    vandermonde_matrix = [
        [sum_t0, sum_t1, sum_t2],
        [sum_t1, sum_t2, sum_t3],
        [sum_t2, sum_t3, sum_t4]
    ]

    A = np.array(vandermonde_matrix)
    b = np.array([sum_yi, sum_ty, sum_t2y])
    return A, b


ti = np.array([0, 1, 2])
yi = np.array([1, 2, 3])
A, b = vandermonde3(ti, yi)
print("A =", A)
print("b =", b)



#Task 1.2
def quadratic_regression(ti, yi):
    """
        Applies quadratic regression to measurement points using a 3x3 Vandermonde matrix
        and fitting a quadratic regression model in the form  a0 + a1*t + a2*t^2

        Parameters:
        ti (array): Measurement points
        yi (array): Measurement values corresponding to ti

        Returns:
        a (array): the coefficients [a0, a1, a2] for the fitted quadratic function
    """
    A, b = vandermonde3(ti, yi)
    x = np.linalg.solve(A, b)
    return x


#Task 1.3
data = np.loadtxt("juggling.txt", skiprows=1)

ti = data[:, 0]
yi = data[:, 1]
[a0, a1, a2] = quadratic_regression(ti, yi)

time_smooth = np.linspace(min(ti), max(ti), 100)


height_fitted = a0 + a1 * time_smooth + a2 * time_smooth**2
plt.plot(ti, yi, 'ro', label="Original data")
plt.plot(time_smooth, height_fitted, 'b-', label="Fitted curve")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Quadratic Fit of Ball Trajectory")
plt.legend()
plt.grid(True)
plt.show()


#Task 2.1
def interpolate_linear(ti, yi, tj, default = 0):
    """
        Applies linear interpolation to unordered sample data in order to estimate values at specified points.

        Parameters:
        ti (array): Measurement points of the sample data
        yi (array): Measurement values corresponding to ti
        tj (array): desired interpolation points
        default: value representing tj points that are beyond the range (default = 0)

        Returns:
        yj (array): interpolated values corresponding to tj
    """

    sorted_indices = np.argsort(ti)
    ti_sorted = ti[sorted_indices]
    yi_sorted = yi[sorted_indices]
    yj = []
    for i in tj:
        if i < ti_sorted[0] or i > ti_sorted[-1]:
            yj.append(default)
        else:
            for k in range(len(ti_sorted) - 1):
                if ti_sorted[k] <= i <= ti_sorted[k+1]:
                    t0 = ti_sorted[k]
                    t1 = ti_sorted[k + 1]
                    y0 = yi_sorted[k]
                    y1 = yi_sorted[k + 1]

                    y_interpolated = y0 + ((i - t0) / (t1 - t0)) * (y1 - y0)
                    yj.append(y_interpolated)
                    break

    return np.array(yj)

#task 2.2
def integrate_composite_trapezoid(tj,yj):
    """
    Uses numerical integration to estimate the value of the area under the curve at specific intervals by
    summing the area of the trapezoids within the bounds

    Parameters:
    tj (array): measurement points over the interval [a,b] (equal spacing)
    yj (array): function values corresponding to the points at tj

    Returns:
    integral (float): Numerical approximation of the area under the curve
    """

    h = tj[1] - tj[0]
    integral = 0

    for i in range(len(tj) - 1):
        area = (h/2) *(yj[i] + yj[i+1])
        integral += area

    return integral

#task 2.3
data = np.loadtxt("distribution.txt", skiprows=1)
ti = data[:, 0]
yi = data[:,1]
n = int(input("Enter number of interpolated points: "))
tj = np.linspace(0,1,n)
interpolated_values = interpolate_linear(ti, yi, tj, default = 0)

e_function = tj * interpolated_values
expected_value = integrate_composite_trapezoid(tj, e_function)

plt.plot(ti, yi, 'b*', label='Original Data')
plt.plot(tj, interpolated_values, 'ro', label='Interpolated Data')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Linear Interpolation of Distribution')
plt.legend()
plt.grid(True)
plt.show()

print(f"Expected value: {expected_value:.3f}")




