import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("emails.csv")

# Top Senders
sender = df['From'].value_counts().head(10)

print("Top Email Senders")
print(sender)

plt.figure(figsize=(8,5))
sender.plot(kind='bar')
plt.title("Top Email Senders")
plt.xlabel("Sender")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.show()

# Top Recipients
recipient = df['To'].value_counts().head(10)

print("\nTop Email Recipients")
print(recipient)

plt.figure(figsize=(8,5))
recipient.plot(kind='bar')
plt.title("Top Email Recipients")
plt.xlabel("Recipient")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.show()
