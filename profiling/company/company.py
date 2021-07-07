"""

"""
import pandas as pd
import numpy as np
from tqdm import tqdm


class Company:
    """

    """

    def __init__(self, num_representatives, range_and_commission_rate):
        """

        Args:
            num_representatives:
            range_and_commission_rate:
        """
        self.num_representatives = num_representatives
        self.range_and_commission_rate = range_and_commission_rate

    def calc_commission_rate(self, sale_percentage):
        """

        Args:
            range_and_commission_rate:
            sale_percentage:

        Returns:

        """
        for limit, rate in self.range_and_commission_rate:
            if sale_percentage <= limit:
                return rate / 100

    def calc_sales(self, sales_target_values, sales_target_prob,
                   average_percentage_to_target,
                   standard_deviation_percentage_to_target,
                   num_simulations=50):

        """

        Args:
            sales_target_values:
            sales_target_prob:
            average_percentage_to_target:
            standard_deviation_percentage_to_target:
            num_simulations:

        Returns:

        """
        all_stats = []

        for i in tqdm(range(num_simulations)):
            # Choose random inputs for the sales targets and percent to target
            sales_target = np.random.choice(sales_target_values, self.num_representatives, p=sales_target_prob)
            pct_to_target = np.random.normal(average_percentage_to_target,
                                             standard_deviation_percentage_to_target,
                                             self.num_representatives).round(2)

            # Build the dataframe based on the inputs and number of reps
            df = pd.DataFrame(index=range(self.num_representatives), data={'Pct_To_Target': pct_to_target,
                                                                           'Sales_Target': sales_target})

            # Back into the sales number using the percent to target rate
            df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

            # Determine the commissions rate and calculate it
            df['Commission_Rate'] = df['Pct_To_Target'].apply(self.calc_commission_rate)
            df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']

            # We want to track sales,commission amounts and sales targets over all the simulations
            all_stats.append([df['Sales'].mean().round(0),
                              df['Commission_Amount'].mean().round(0),
                              df['Sales_Target'].mean().round(0)])

        return pd.DataFrame.from_records(all_stats, columns=['Sales',
                                                             'Commission_Amount',
                                                             'Sales_Target'])
