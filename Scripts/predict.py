from load_dataset import load_dataset, split_dataset
from train import train_model
import pandas as pd
import tensorflow_decision_forests as tfdf

# Load and prepare the dataset
train_df = load_dataset("Data/train.csv")
print("Dataset loaded successfully")
print("Dataset shape is {}".format(train_df.shape))

train_set, valid_set = split_dataset(train_df, 0.2)
print("{} examples in training, {} examples in testing.".format(len(train_set), len(valid_set)))

# Load and train the model
rf_model = train_model(train_set, valid_set)

# Predict on the test dataset
test_df = load_dataset("Data/test.csv")
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_df, task = tfdf.keras.Task.REGRESSION)

preds = rf_model.predict(test_ds)

output = pd.DataFrame({'SalePrice': preds.squeeze()}) # Create a DataFrame containing the predictions
print("/nFirst 5 predictions:")
print(output.head())

output.to_csv('Results/submission.csv', index=False) # Save the predictions to a CSV file