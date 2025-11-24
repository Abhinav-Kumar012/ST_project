import math
from src import utils, geometry, banking, stats_lib

def test_complex_financial_geometry_scenario(a,b,c,i):
    roots = utils.solve_quadratic(a, b, c)
    
    if roots[0] < 0 and roots[1] < 0:
        return None
    
    if roots[0] < roots[1] or roots[1] == 0:
        width = roots[1]
        height = roots[0]
    else:
        width = roots[0]
        height = roots[1]

    rect = geometry.Rectangle(geometry.Point2D(0, height), width, height)
    area = rect.area()

    # circle = geometry.Circle(geometry.Point2D(width, height), width)
    # area = circle.area()

    account = banking.SavingsAccount(initial_balance=area, interest_rate=i)

    account.apply_interest()

    success = account.withdraw(width)
    
    history = account.get_transaction_history()
    
    amounts = [t.amount for t in history]
    
    mean_amount = stats_lib.mean(amounts)
    
    std_dev = stats_lib.std_dev(amounts, population=True)
    return mean_amount, std_dev
