"""
Test Company
"""
import pytest
import cProfile
import io
import pstats
from pstats import SortKey
from profiling.company.company import Company

Enacom = Company(num_representatives=10,
                 range_and_commission_rate=[(0.9, 2), (.99, 3), (1, 4)])


@pytest.mark.parametrize("method", [Enacom.financial_projections,
                                    Enacom.financial_projections_1,
                                    Enacom.financial_projections_2])
def test_financial_projections_100(method):
    """

    Args:
        method:

    Returns:

    """
    sales_target_values = [10_000]
    sales_target_prob = [1]
    sales = method(sales_target_values=sales_target_values,
                   sales_target_prob=sales_target_prob,
                   average_percentage_to_target=1,
                   standard_deviation_percentage_to_target=0.,
                   num_simulations=5)
    assert [sales['Sales'].mean(),
            sales['Commission_Amount'].mean(),
            sales['Sales_Target'].mean()] == [100000, 4000, 100000]


@pytest.mark.parametrize("method", [Enacom.financial_projections,
                                    Enacom.financial_projections_1,
                                    Enacom.financial_projections_2])
def test_financial_projections_90(method):
    sales_target_values = [10_000]
    sales_target_prob = [1]
    sales = method(sales_target_values=sales_target_values,
                   sales_target_prob=sales_target_prob,
                   average_percentage_to_target=0.9,
                   standard_deviation_percentage_to_target=0.,
                   num_simulations=5)
    assert [sales['Sales'].mean(),
            sales['Commission_Amount'].mean(),
            sales['Sales_Target'].mean()] == [90000., 1800., 100000.]


@pytest.mark.parametrize("method", [Enacom.financial_projections,
                                    Enacom.financial_projections_1,
                                    Enacom.financial_projections_2])
def test_financial_projections_99(method):
    sales_target_values = [10_000]
    sales_target_prob = [1]
    sales = method(sales_target_values=sales_target_values,
                   sales_target_prob=sales_target_prob,
                   average_percentage_to_target=0.99,
                   standard_deviation_percentage_to_target=0.,
                   num_simulations=5)
    assert [sales['Sales'].mean(),
            sales['Commission_Amount'].mean(),
            sales['Sales_Target'].mean()] == [99000., 2970., 100000.]
