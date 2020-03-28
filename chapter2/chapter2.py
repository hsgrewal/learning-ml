import os
import tarfile
import urllib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from zlib import crc32
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

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

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing = load_housing_data()

def show_data(data, data_msg):
    # Quick look at the data
    print("\n" + data_msg + " - Top 5 Rows:")
    print(data.head())

    # Show amount of data
    print("\n" + data_msg + " - Length:")
    print(len(data))

    # Show info about data
    print("\n" + data_msg + " - Data Info:")
    print(data.info())

    # Show details of particular field
    print("\n" + data_msg + " - Value Counts for Ocean Proximity field:")
    print(data["ocean_proximity"].value_counts())

    # Show summary of data
    print("\n" + data_msg + " - Summary")
    print(data.describe())

    # Show histogram of data
    data.hist(bins=50, figsize=(20,15))
    plt.show()

#show_data(housing, "Raw Housing Data")

## Create a Test Set and a Train Set
#train_set, test_set = split_train_test(housing, 0.2)
#show_data(train_set, "Train Data")
#show_data(test_set, "Test Data")

#housing_with_id = housing.reset_index()     # add an 'index' column
# Use more stable method for id
#housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
#train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
#show_data(train_set, "Train Data")
#show_data(test_set, "Test Data")

housing["income_cat"] = pd.cut(housing["median_income"],
                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                labels=[1, 2, 3, 4, 5])
#housing["income_cat"].hist()
#plt.show()

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

#print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing = strat_train_set.copy()
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
