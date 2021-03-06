"""
Simulation
"""
import matplotlib.pyplot as plt
from profiling.company.company import Company

Enacom = Company(num_representatives=500,
                 range_and_commission_rate=[(0.9, 2), (.99, 3), (1, 4)])

sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]
sales = Enacom.financial_projections_2(sales_target_values=sales_target_values,
                                       sales_target_prob=sales_target_prob,
                                       average_percentage_to_target=1,
                                       standard_deviation_percentage_to_target=0.1,
                                       num_simulations=200)
# plt.figure()
# sales['Commission_Amount'].plot(kind='hist', title="Total Commission Amount")
# plt.show()
# plt.figure()
# sales['Sales'].plot(kind='hist', title="Total Sales")
# plt.show()
# plt.figure()
# sales['Sales_Target'].plot(kind='hist', title="Total Sales Target")
# plt.show()
