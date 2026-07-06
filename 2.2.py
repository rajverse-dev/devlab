import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("emails.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['Date'])

# Extract Month
df['Month'] = df['Date'].dt.month_name()

# Count emails per month
monthly = df['Month'].value_counts()

print(monthly)

# Plot graph
monthly.plot(kind='bar')
plt.title("Emails Sent Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Emails")
plt.show()
