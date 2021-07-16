<h1>Examples Profiling</h1>

> Status: Done

## Introduction 

## Installation Profiling
```
pip install profiling
```

## Installation snakeviz 
```
pip install snakeviz
```

# Run Profiling in Code

```
import cProfile 
cProfile.run('company.financial_projections_1(sales_target_values=sales_target_values,\
                          sales_target_prob=sales_target_prob,\
                          average_percentage_to_target=average_percentage_to_target,\
                          standard_deviation_percentage_to_target=standard_deviation_percentage_to_target,\
                          num_simulations=num_simulations))')
```

# Run Profiling in terminal
```
python -m cProfile -o temp_0.dat profiling/simulation/simulation.py

```
# Run snakeviz
```
snakeviz temp_0.dat
```
