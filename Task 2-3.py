import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(0)
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100),
    'Value': np.random.randn(100)
}
df = pd.DataFrame(data)
# Create a box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Category', y='Value', data=df)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot of Value by Category')
plt.grid(True)
plt.show()
