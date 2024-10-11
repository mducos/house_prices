import pandas as pd
import numpy as np

def load_dataset(data_path: str) -> pd.DataFrame:
    """
    Load the dataset from the given path

    :param data_path: Path to the dataset
    :return: DataFrame containing the dataset
    """

    dataset_df = pd.read_csv(data_path)

    dataset_df = dataset_df.drop('Id', axis=1) # Drop the Id column as it is not necessary

    return dataset_df

def split_dataset(dataset, test_ratio=0.20):
    """
    Split the dataset into training and testing sets

    :param dataset: DataFrame containing the dataset
    :param test_ratio: Ratio of the dataset to be used for testing
    :return: Tuple containing the training and testing sets
    """
  
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]
