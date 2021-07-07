"""
Test Company
"""
import pytest
import cProfile
import io
import pstats
from pstats import SortKey
from profiling.company.company import Company


@pytest.fixture(scope="module")
def enacom():
    Enacom = Company(num_representatives=500,
                     range_and_commission_rate=[(0.9, 2), (.99, 3), (1, 4)])

    sales_target_values = [100_000]
    sales_target_prob = [1]
    sales = Enacom.calc_sales(sales_target_values=sales_target_values,
                              sales_target_prob=sales_target_prob,
                              average_percentage_to_target=1,
                              standard_deviation_percentage_to_target=0.,
                              num_simulations=2000)
    return sales


def test_sales(enacom):
    assert enacom['Sales'].mean() == 100000


def test_commission_amount(enacom):
    assert enacom["Commission_Amount"].mean() == 0.04*100000


def test_sales_target(enacom):
    assert enacom['Sales'].mean() == 100000
