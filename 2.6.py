import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("emails.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['Date'])

# Create numerical features
df['Subject_Length'] = df['Subject'].fillna('').apply(len)
df['Hour'] = df['Date'].dt.hour

# Correlation Matrix
corr = df[['Subject_Length', 'Hour']].corr()

print("Correlation Matrix")
print(corr)

# Heatmap
plt.imshow(corr, cmap='coolwarm')
plt.colorbar()
plt.xticks([0,1], ['Subject_Length','Hour'])
plt.yticks([0,1], ['Subject_Length','Hour'])
plt.title("Correlation Matrix")
plt.show()
