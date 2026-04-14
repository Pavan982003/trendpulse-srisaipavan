import pandas as pd
import os

# -------------------------------
# Step 1 — Load JSON file
# -------------------------------


file_path = "C:/Users/HI/Downloads/masai/data/trends_20260412.json"

# Check if file exists
if not os.path.exists(file_path):
    print("File not found. Please check the file name.")
    exit()

# Load JSON into DataFrame
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# -------------------------------
# Step 2 — Data Cleaning
# -------------------------------

# Remove duplicates based on post_id
df = df.drop_duplicates(subset=["post_id"])
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing important values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra spaces in title
df["title"] = df["title"].str.strip()

# -------------------------------
# Step 3 — Save as CSV
# -------------------------------

output_path = "data/trends_clean.csv"

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Save cleaned data
df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")

# -------------------------------
# Step 4 — Summary
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())