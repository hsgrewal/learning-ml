import os
import tarfile
import urllib
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

# Quick look at the data
housing = load_housing_data()
print(housing.head())

# Show info about data
print(housing.info())

# Show details of particular field
print(housing["ocean_proximity"].value_counts())

# Show summary of data
print(housing.describe())

# Show histogram of data
housing.hist(bins=50, figsize=(20,15))
plt.show()
