#### https://medium.com/@abuolubunmi21/improve-your-python-skills-with-type-hinting-3496d422fe24
from typing import Tuple, NewType
import numpy as np
import numpy.typing as npt


# SYNTAX
# variable_name or type_alias = NewType(name: str, base: type) -> type_alias

# Create the custom type
TrainTestDataset = NewType("TrainTestDataset", Tuple[npt.NDArray[np.float64], 
                                                     npt.NDArray[np.float32], 
                                                     npt.NDArray[np.float64], 
                                                     npt.NDArray[np.float32]])

# Function to split the dataset and return the custom type
def prepare_dataset(data: np.ndarray, labels: np.ndarray, test_size: float = 0.2) -> TrainTestDataset:
    # Assume `data` is a 2D array of features and `labels` is a 1D array of labels
    # We want to split the data into training and test sets
    split_index = int(len(data) * (1 - test_size))
    train_data = data[:split_index]
    test_data = data[split_index:]
    
    train_labels = labels[:split_index]
    test_labels = labels[split_index:]
    
    
    return TrainTestDataset((train_data.astype(np.float64), 
                             train_labels.astype(np.float32), 
                             test_data.astype(np.float64), 
                             test_labels.astype(np.float32)))

# Sample data
data = np.random.rand(100, 5)  
labels = np.random.randint(0, 2, size=100)  

# Prepare the dataset
dataset = prepare_dataset(data, labels)

print(type(dataset))          # Output: <class 'typing.NewType'>

print(dataset)