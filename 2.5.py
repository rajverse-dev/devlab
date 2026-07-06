import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("emails.csv")

# Extract email domain
df['Domain'] = df['From'].str.split('@').str[1]

# Count domains
domain = df['Domain'].value_counts()

print("Email Domain Count")
print(domain)

# Plot graph
domain.plot(kind='bar')
plt.title("Email Domain Analysis")
plt.xlabel("Domain")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.show()
