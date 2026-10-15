import numpy as np
import pandas as pd

df = pd.read_csv("deals.csv")
customers = pd.read_csv("customers.csv") 

deals = df.copy()
def EDA(deals : pd.DataFrame) -> pd.DataFrame:

    deals["source"] = deals["source"].str.strip().str.lower()                 # deleting the leading and trailing space and lowering
    deals["status"] = deals["status"].str.strip().str.lower()


    deals["source"] = deals["source"].fillna("unknown")                       # filling with unknown, must be checked later
    deals["status"] = deals["status"].fillna("unknown")


    print("Duplicates removed:", deals.duplicated().sum())
    deals = deals.drop_duplicates().copy()                                       # We can delete the duplicates, after checking if the customer didnt really make the same exact deal twice


    print("Negative amounts:", (deals["amount"] < 0).sum())
    deals.loc[deals["amount"] < 0, "amount"] = np.nan                    # again needs checking


    deals["amount_missing"] = deals["amount"].isna()
    deals["amount_suspicious"] = (deals["amount"] == 0) | (deals["amount"] > 10000)      # we can set the upper limit for our deal amount, I chose 10000 conditionally  


    difference = set(deals["customer_id"]).difference(set(customers["customer_id"]))
    if len(difference) != 0:
        deals.drop(                                                     # there cant be deals that dont have customers, but there can be customers that dont have deals thats why I am checking only on one side, this is a one to many connection in SQL terms
            deals[deals["customer_id"].isin(difference)].index, inplace = True
        )

    print("Deals removed because of non-existing customer id : ", len(difference))

    deals.to_csv("deals_clean.csv", index=False)

    return deals

deals = EDA(deals)

