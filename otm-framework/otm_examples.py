import numpy as np

from science_optimization.algorithms.cutting_plane import EllipsoidMethod
from science_optimization.solvers import Optimizer
from science_optimization.solvers.pareto_samplers import NonDominatedSampler, EpsilonSampler, MuSampler, LambdaSampler

from science_optimization.problems import GenericProblem

from science_optimization.builder import OptimizationProblem

from science_optimization.function import LinearFunction, QuadraticFunction, GenericFunction


def plot_example():

    # Plot functions
    Q = np.array([[3, 0], [0, 1]])
    c = np.array([[8], [1]])
    d = 4

    # defining function object
    l_func = LinearFunction(c=c, d=8)
    q_func = QuadraticFunction(Q=Q, c=c, d=d)

    # plot function eval
    x_lim = np.array([[-5, 5], [-5, 5]])
    # q_func.plot(x_lim)
    # l_func.plot(x_lim)

    # _____________________________________________________
    # Plot mono objective optimization
    generic = OptimizationProblem(
        builder=GenericProblem(f=[q_func], eq_cons=[], ineq_cons=[l_func], x_bounds=x_lim)
    )
    optimizer = Optimizer(
        opt_problem=generic,
        algorithm=EllipsoidMethod(x0=np.array([[-4], [-4]]))
    )
    results = optimizer.optimize(debug=False)
    results.info()
    # generic.plot()

    # ____________________________________________________
    # Plot pareto sample data (example 1)
    f = [l_func, q_func]
    generic = OptimizationProblem(builder=GenericProblem(f=f, eq_cons=[], ineq_cons=[], x_bounds=x_lim))
    sampler = NonDominatedSampler(optimization_problem=generic, distance_type=1)
    # sampler = EpsilonSampler(optimization_problem=generic, objective_constraint_index=0)
    # sampler = MuSampler(optimization_problem=generic)
    # sampler = LambdaSampler(optimization_problem=generic)

    sampler.sample()

    generic.plot()

    # ____________________________________________________
    # Plot pareto sample data (example 2)

    # objective function 1
    def f_obj1(x): return np.max(np.abs(x * (.5 + 1e-2) - .5 * np.sin(x) * np.cos(x)), axis=0)

    # parameters objective function 2
    Q = np.array([[10, 9], [9, 10]])
    c = np.array([[-90], [-100]])
    d = np.array([250])

    x_lim = np.array([[-5, 10], [-5, 10]])

    # objectives
    f1 = GenericFunction(func=f_obj1, n=2)
    f2 = QuadraticFunction(Q=Q, c=c, d=d)

    f2.plot(x_lim)
    f2.plot(x_lim, levels=[10, 100])
    f = [f1, f2]
    generic = OptimizationProblem(builder=GenericProblem(f=f, eq_cons=[], ineq_cons=[], x_bounds=x_lim))

    # sampler = LambdaSampler(optimization_problem=generic)
    # sampler = EpsilonSampler(optimization_problem=generic, objective_constraint_index=1)
    sampler = NonDominatedSampler(optimization_problem=generic)

    sampler.sample()

    generic.plot()

    # with 3 objectives
    Q = np.array([[1, 0], [0, 1]])
    c1 = np.array([[0], [0]])
    d1 = np.array([0])

    # parameters objective function 2
    c2 = np.array([[-2], [-2]])
    d2 = np.array([2])

    # parameters objective function 3
    c3 = np.array([[2], [-2]])
    d3 = np.array([2])

    # objectives
    f1 = QuadraticFunction(Q=Q, c=c1, d=d1)
    f2 = QuadraticFunction(Q=Q, c=c2, d=d2)
    f3 = QuadraticFunction(Q=Q, c=c3, d=d3)
    f = [f1, f3, f2]

    # constraints
    ineq_cons = []
    eq_cons = []

    # bounds
    x_min = np.array([-5, -5]).reshape(-1, 1)  # lower
    x_max = np.array([5, 5]).reshape(-1, 1)  # upper
    x_lim = np.hstack((x_min, x_max))

    # build generic problem instance
    generic = OptimizationProblem(builder=GenericProblem(f=f, eq_cons=eq_cons, ineq_cons=ineq_cons, x_bounds=x_lim))

    # builder pareto sampler
    sampler = EpsilonSampler(optimization_problem=generic, n_samples=18, n_layers=3, objective_constraint_index=1)
    results = sampler.sample()

    results.info()

    # contour plot of functions and solutions (variables and objective space)
    generic.plot(levels=[1])


if __name__ == "__main__":
    # run problem example
    plot_example()
