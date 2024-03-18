import pandas as pd
import numpy as np

# Crear un DataFrame con datos aleatorios
data = {
    'A': np.random.randn(10),
    'B': np.random.rand(10),
    'C': np.random.randint(1, 100, size=10),
    'D': np.random.choice(['apple', 'banana', 'cherry'], size=10)
}

df = pd.DataFrame(data)

df.to_csv("job1.csv",index=False)