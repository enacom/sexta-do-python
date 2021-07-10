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


@pytest.mark.parametrize("method", [Enacom.calc_sales,
                                    Enacom.calc_sales_1,
                                    Enacom.calc_sales_2])
def test_sales(method):
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
            sales['Sales_Target'].mean()] == [100000, 20000, 100000]


@pytest.mark.parametrize("method", [Enacom.calc_sales,
                                    Enacom.calc_sales_1,
                                    Enacom.calc_sales_2])
def test_commission_amount(enacom):
    assert enacom["Commission_Amount"].mean() == 0.04 * 100000


def test_sales_target(enacom):
    assert enacom['Sales'].mean() == 100000
