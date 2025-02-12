#### https://medium.com/@abuolubunmi21/improve-your-python-skills-with-type-hinting-3496d422fe24

import pandas as pd
import numpy as np
import numpy.typing as npt
from typing import Tuple

def calculate_mean_and_std(data: pd.DataFrame) -> Tuple[npt.NDArray[np.float64],
    npt.NDArray[np.float64]]:
    
    numerical_data = data.select_dtypes(include=np.number)
    means = numerical_data.mean().values.astype(np.float64)
    stds = numerical_data.std().values.astype(np.float64)

    return means, stds

if __name__ == "__main__":

    data = {
        'A': [1, 2, 3],
        'B': [4.4, 5.9, 6.0],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    mean_values, std_values = calculate_mean_and_std(df)
    print("Mean values:", mean_values)
    print("Standard deviation values:", std_values)