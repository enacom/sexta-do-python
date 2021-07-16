"""
Company Class
"""
import pandas as pd
import numpy as np
from tqdm import tqdm


class Company:
    """
    Company Class
    """

    def __init__(self, num_representatives, range_and_commission_rate):
        """
        Create a company with a certain number of employees and fixed commission rates.

        Args:
            num_representatives: (int) number of company representatives.
            range_and_commission_rate: (list) list of tuples with ranges and commission values respectively.
        """
        self.num_representatives = num_representatives
        self.range_and_commission_rate = range_and_commission_rate

    def calc_commission_rate(self, sale_percentage):
        """
        This function returns the commission rate the employee
        will earn based on their sales percentage.

        Args:
            sale_percentage: (float) sales percentage of a representatives.

        Returns:
            rate: (float) commission rate.
        """
        for limit, percentage_rate in self.range_and_commission_rate:
            if limit < sale_percentage:
                rate = percentage_rate / 100
            else:
                rate = percentage_rate / 100
                break
        return rate

    def financial_projections(self, sales_target_values, sales_target_prob,
                              average_percentage_to_target,
                              standard_deviation_percentage_to_target,
                              num_simulations=50):

        """
         Creates financial projection for total comission, total sales and total sales target for the company.
        Args:
            sales_target_values: (list)  List of target sales values.
            sales_target_prob: (list) List with distribution of target sales values.
            average_percentage_to_target: (float) Avarage value of sales percentage to the representatives.
            standard_deviation_percentage_to_target: (float) Standard deviation of sales percentage to the repreentatives.
            num_simulations: Number of simulation tests.

        Returns:
            projections: (Dataframe) Dataframe with total comission, total sales and total sales target.

        """
        all_stats = []

        for i in tqdm(range(num_simulations)):
            # Choose random inputs for the sales targets and percent to target
            sales_target = np.random.choice(sales_target_values,
                                            self.num_representatives,
                                            p=sales_target_prob)
            pct_to_target = np.random.normal(average_percentage_to_target,
                                             standard_deviation_percentage_to_target,
                                             self.num_representatives).round(2)

            # Build the dataframe based on the inputs and number of reps
            df = pd.DataFrame(index=range(self.num_representatives),
                              data={'Pct_To_Target': pct_to_target,
                                    'Sales_Target': sales_target})

            # Back into the sales number using the percent to target rate
            df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

            # Determine the commissions rate and calculate it
            df1 = pd.DataFrame(columns=["Commission_Rate", 'Commission_Amount'])
            for j in range(len(df)):
                commission_rate = self.calc_commission_rate(df['Pct_To_Target'][j])
                commission_amount = commission_rate * df['Sales'][j]
                df1.loc[j] = [commission_rate, commission_amount]
            df = pd.concat([df, df1], axis=1)
            # We want to track sales,commission amounts and sales targets over all the simulations
            all_stats.append([df['Sales'].sum().round(0),
                              df['Commission_Amount'].sum().round(0),
                              df['Sales_Target'].sum().round(0)])

        return pd.DataFrame.from_records(all_stats, columns=['Sales',
                                                             'Commission_Amount',
                                                             'Sales_Target'])

    def financial_projections_1(self, sales_target_values, sales_target_prob,
                                average_percentage_to_target,
                                standard_deviation_percentage_to_target,
                                num_simulations=50):

        """
         Creates financial projection for total comission, total sales and total sales target for the company.
        Args:
            sales_target_values: (list)  List of target sales values.
            sales_target_prob: (list) List with distribution of target sales values.
            average_percentage_to_target: (float) Avarage value of sales percentage to the representatives.
            standard_deviation_percentage_to_target: (float) Standard deviation of sales percentage to the repreentatives.
            num_simulations: Number of simulation tests.

        Returns:
            projections: (Dataframe) Dataframe with total comission, total sales and total sales target.

        """
        all_stats = []

        for i in tqdm(range(num_simulations)):
            # Choose random inputs for the sales targets and percent to target
            sales_target = np.random.choice(sales_target_values,
                                            self.num_representatives,
                                            p=sales_target_prob)
            pct_to_target = np.random.normal(average_percentage_to_target,
                                             standard_deviation_percentage_to_target,
                                             self.num_representatives).round(2)

            # Build the dataframe based on the inputs and number of reps
            df = pd.DataFrame(index=range(self.num_representatives),
                              data={'Pct_To_Target': pct_to_target,
                                    'Sales_Target': sales_target})

            # Back into the sales number using the percent to target rate
            df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

            # Determine the commissions rate and calculate it
            df['Commission_Rate'] = df['Pct_To_Target'].apply(self.calc_commission_rate)
            df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']

            # We want to track sales,commission amounts and sales targets over all the simulations
            all_stats.append([df['Sales'].sum().round(0),
                              df['Commission_Amount'].sum().round(0),
                              df['Sales_Target'].sum().round(0)])

        return pd.DataFrame.from_records(all_stats, columns=['Sales',
                                                             'Commission_Amount',
                                                             'Sales_Target'])

    def financial_projections_2(self, sales_target_values, sales_target_prob,
                                average_percentage_to_target,
                                standard_deviation_percentage_to_target,
                                num_simulations=50):

        """
         Creates financial projection for total comission, total sales and total sales target for the company.
        Args:
            sales_target_values: (list)  List of target sales values.
            sales_target_prob: (list) List with distribution of target sales values.
            average_percentage_to_target: (float) Avarage value of sales percentage to the representatives.
            standard_deviation_percentage_to_target: (float) Standard deviation of sales percentage to the repreentatives.
            num_simulations: Number of simulation tests.

        Returns:
            projections: (Dataframe) Dataframe with total comission, total sales and total sales target.

        """
        all_stats = np.zeros((num_simulations, 3))

        for i in tqdm(range(num_simulations)):
            # Choose random inputs for the sales targets and percent to target
            sales_target = np.random.choice(sales_target_values,
                                            self.num_representatives,
                                            p=sales_target_prob)
            pct_to_target = np.random.normal(average_percentage_to_target,
                                             standard_deviation_percentage_to_target,
                                             self.num_representatives).round(2)

            # Build the dataframe based on the inputs and number of reps
            sales = sales_target * pct_to_target

            # Determine the commissions rate and calculate it
            commission_rate = np.array([self.calc_commission_rate(xi) for xi in pct_to_target])
            commission_amount = commission_rate * sales

            # We want to track sales,commission amounts and sales targets over all the simulations
            all_stats[i, :] = [sales.sum(), commission_amount.sum(), sales_target.sum()]

        return pd.DataFrame.from_records(all_stats, columns=['Sales',
                                                             'Commission_Amount',
                                                             'Sales_Target'])
