import pandas as pd
import numpy as np
import os

# -------------------------------
# Step 1 — Load and Explore
# -------------------------------

file_path = "data/trends_clean.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("File not found. Please run Task 2 first.")
    exit()

# Load CSV
df = pd.read_csv(file_path)

print(f"Loaded data: {df.shape}")

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# -------------------------------
# Step 2 — Analysis using NumPy
# -------------------------------

scores = df["score"].values   # convert to NumPy array

print("\n--- NumPy Stats ---")

# Mean, median, std
print(f"Mean score   : {np.mean(scores):.2f}")
print(f"Median score : {np.median(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")

# Max and Min
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(f"\"{max_comments_row['title']}\" — {max_comments_row['num_comments']} comments")

# -------------------------------
# Step 3 — Add New Columns
# -------------------------------

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular if score > average score
df["is_popular"] = df["score"] > avg_score

# -------------------------------
# Step 4 — Save Result
# -------------------------------

output_path = "data/trends_analysed.csv"

# Create folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")