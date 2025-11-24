from src import integration
mean_amount, std_dev = integration.test_complex_financial_geometry_scenario(1, -3, 0,0.1)
print(mean_amount, std_dev)
