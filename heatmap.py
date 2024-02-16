import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Example confusion matrix
actual_labels = [1, 0, 1, 2, 0, 1, 2, 0, 2]
predicted_labels = [1, 0, 1, 2, 0, 1, 0, 0, 2]
cm = confusion_matrix(actual_labels, predicted_labels)

# Create a heatmap using Seaborn
sns.set(font_scale=2)  # Adjust font size for better readability

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", linewidths=.5, square=True, cbar_kws={"shrink": 0.75}, xticklabels=[0, 1, 2], yticklabels=[0, 1, 2])

plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()
