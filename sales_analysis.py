import pandas as pd

data = pd.read_csv("amazon.csv")

print(data.head())
print(data.shape)
print(data.columns)

print("\ndataset information:")
print(data.info())

print("\nmissing values:")
print(data.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

print(data.head())

# Count products in each category
category_counts = data["category"].value_counts().head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.values, y=category_counts.index)

plt.title("Top 10 Amazon Product Categories")
plt.xlabel("Number of Products")
plt.ylabel("Category")
plt.tight_layout()

plt.show()

# Product Ratings Analysis
data["rating"] = pd.to_numeric(data["rating"], errors="coerce")

plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="rating", bins=10)

plt.title("Amazon Product Ratings Distribution")
plt.xlabel("Product Rating")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.show()
# Product Price Analysis
data["discounted_price"] = data["discounted_price"].astype(str).str.replace(",", "", regex=False)
data["discounted_price"] = data["discounted_price"].str.replace("₹", "", regex=False)
data["discounted_price"] = pd.to_numeric(data["discounted_price"], errors="coerce")

plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="discounted_price", bins=20)

plt.title("Amazon Product Price Distribution")
plt.xlabel("Discounted Price (₹)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.show()

# Product Rating vs Discounted Price

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="rating",
    y="discounted_price"
)

plt.title("Product Rating vs Discounted Price")
plt.xlabel("Product Rating")
plt.ylabel("Discounted Price (₹)")
plt.tight_layout()
plt.show()