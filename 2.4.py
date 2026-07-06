import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load dataset
df = pd.read_csv("emails.csv")

# Subject Length
df['Subject_Length'] = df['Subject'].fillna('').apply(len)

print("Subject Length")
print(df['Subject_Length'])

# Combine all subjects
text = " ".join(df['Subject'].fillna('').astype(str))

# Find frequent words
words = re.findall(r'\w+', text.lower())
common = Counter(words).most_common(10)

# Display words
freq = pd.DataFrame(common, columns=['Word','Count'])
print("\nMost Frequent Words")
print(freq)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(freq['Word'], freq['Count'])
plt.title("Most Frequent Words in Email Subjects")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
