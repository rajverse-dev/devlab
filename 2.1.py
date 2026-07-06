import mailbox
import pandas as pd

path = r"C:\Users\Rahul\OneDrive\Documents\DEV\Takeout\Mail\All mail Including Spam and Trash.mbox"

mbox = mailbox.mbox(path)

print("Total Emails:", len(mbox))


# Extract email details
data = []

for message in mbox:
    data.append({
        "Date": message["Date"],
        "From": message["From"],
        "To": message["To"],
        "Subject": message["Subject"]
    })

# Create DataFrame
df = pd.DataFrame(data)

print("\nFirst Five Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nShape of Dataset")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# Save as CSV
df.to_csv("emails.csv", index=False)

print("\nCSV file created successfully.")
