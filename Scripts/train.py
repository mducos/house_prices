import tensorflow_decision_forests as tfdf

def train_model(train_df, valid_df):
    """
    Train a model using the Random Forest algorithm.

    :param train_df: DataFrame containing the training dataset
    :param valid_df: DataFrame containing the validation dataset
    :return: Trained model
    """
  
    label = 'SalePrice'
    train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label=label, task = tfdf.keras.Task.REGRESSION) # Convert the DataFrame to a TensorFlow dataset
    valid_ds = tfdf.keras.pd_dataframe_to_tf_dataset(valid_df, label=label, task = tfdf.keras.Task.REGRESSION)

    rf = tfdf.keras.RandomForestModel(task = tfdf.keras.Task.REGRESSION) # Create a Random Forest model
    rf.compile(metrics=["mse"])
    rf.fit(x=train_ds)

    rf.evaluate(x=valid_ds,return_dict=True) # Evaluate the model on the validation dataset

    return rf