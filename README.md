# House price predictions

This project is derived from the Kaggle competition: [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/).

## Quick explanations of the project

### Goal

The objective is to predict the sales price for each house, specifically the value of the `SalePrice` variable for each ID in the test set.

### Metric

Submissions are evaluated based on the Root Mean Squared Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price.

### Result file format

The result file should contain a header and follow this format:

```
Id,SalePrice
1461,169000.1
1462,187724.1233
1463,175221
```

## Description of the repository

- **Data Folder:** contains the datasets used for training and testing.
- **Scripts Folder:** contains the scripts used for data processing and model training.
- **Results Folder:** contains the output results of the predictions.

## Launch the project

You can launch the project in two ways: via a notebook or through the terminal.

### Terminal instructions

```
python3.9 -m venv house_prices_env
source house_prices_env/bin/activate
pip install -r requirements.txt
```

### Notebook Instructions

You can also run the project using a Jupyter Notebook. Ensure that the environment is set up as described above.

# Data

- ```test.csv```: Contains data for 1460 houses.
- ```train.csv```: Contains data for 1460 houses.

A total of 79 variables must be considered to determine the SalePrice. More details can be found in ```data_description.txt```.