<h1>Examples Profiling</h1>

> Status: Developing

## Introduction 

## Installation Profiling
```
pip install profiling
```

## Installation snakeviz 
```
pip install snakeviz
```

# Profile Example

objective of the example: show profiling examples of how to use profiling



Regra: atendimento da tabela regressiva. Aliquota aplicada sobre o lucro

| Sales Represenative| Sales Target R$ |Actual Sales R$ | Percentage Sales % | commsion rate | Comssion Amount R$ |
|--------------------|-----------------|----------------|--------------------|---------------|-----------------|
| 1                  | 100000          | 88000          | 88                 |     2         | 1760            |
| 2                  | 200000          | 202000         | 101                |     4         | 8080            |
| 3                  | 75000           | 90000          | 120                |     4         | 3600            |

Commission Amount = Actual Sales * Commission Rate

| Percentage Sale | Comsission Rate |
|-----------------|-----------------|
| <= 90%          | 2%              |
| >90 && <=99     | 3%              |
| >= 100%         | 4%              |

Inputs:

    
Outputs:

# Run Profiling in Code

```
import cProfile 
cProfile.run('company.financial_projections_1(sales_target_values=sales_target_values,\
                          sales_target_prob=sales_target_prob,\
                          average_percentage_to_target=average_percentage_to_target,\
                          standard_deviation_percentage_to_target=standard_deviation_percentage_to_target,\
                          num_simulations=num_simulations))')
```
