from scipy.constants import g

L = 0.5
m = 0.1


def pendulum_model(t, y):
    """
    The right-hand side of the pendulum ODE
    """
    theta_1, theta_2, p_1, p_2 = y[0], y[1], y[2], y[3]

    f1 = 6.0 / (m * L**2)

    dcos = np.cos(theta_1 - theta_2)
    dsin = np.sin(theta_1 - theta_2)

    denominator = 16 - 9 * dcos**2

    dtheta_1 = f1 * (2 * p_1 - 3 * dcos * p_2) / denominator
    dtheta_2 = f1 * (8 * p_2 - 3 * dcos * p_1) / denominator

    f2 = -0.5 * m * L**2
    dp_1 = f2 * ( dtheta_1 * dtheta_2 * dsin + 3 * (g / L) * np.sin(theta_1))
    dp_4 = f2 * (-dtheta_1 * dtheta_2 * dsin + (g / L) * np.sin(theta_2))

    return [dtheta_1, dtheta_2, dp_1, dp_4]


# initial values
y0 = [np.pi / 3, -np.pi / 4, 0, 0.065]
t_start, t_end = 0, 20

solution = solve_ivp(pendulum_model, (t_start, t_end), y0, t_eval=np.linspace(t_start, t_end, 40000))

x1s = + L * np.sin(solution.y[0])
y1s = - L * np.cos(solution.y[0])

x2s = x1s + L * np.sin(solution.y[1])
y2s = y1s - L * np.cos(solution.y[1])

plt.plot(x1s, y1s, '.', alpha=0.02)
plt.plot(x2s, y2s, '.', alpha=0.1)
plt.axis('off')
None
