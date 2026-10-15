import pandas as pd
import numpy as np
import random

random.seed(42)

Source = ["Instagram", "Telegram", "Facebook", "Friend/Relative"]
Status = ["Won", "Lost", "In Progress"]

deals= []

for i in range(3000):
    deal = {
    "deal_id" : i + 1,
    "customer_id" : random.randint(1,500),
    "amount" : random.randint(500,5000),    #(f"${random.randint(500,5000)}") This would format the number with $ sign in front, but I kept the numbers as integer for better ML interpretation
    "source" : random.choice(Source),
    "status" : random.choice(Status),
    
    }

    deals.append(deal)


first_names = [
    "Anna", "Aram", "Ani", "David", "Mariam",
    "Narek", "Lilit", "Hayk", "Sona", "Gor"
]

last_names = ["Hakobyan", "Grigoryan", "Sargsyan", "Petrosyan",
    "Harutyunyan", "Gevorgyan", "Hovhannisyan",
    "Mkrtchyan", "Avetisyan", "Manukyan"]

cities = [
    "Yerevan", "Gyumri", "Vanadzor",
    "Vagharshapat", "Abovyan"
]

customers = []

for i in range(1, 501):
    customer = {
        "customer_id": i,
        "name": random.choice(first_names),
        "surname" : random.choice(last_names),
        "city": random.choice(cities),
        "age": random.randint(18, 65)
    }

    customers.append(customer)



deals.extend([
    {
        "deal_id": 3001,
        "customer_id": 158,
        "amount": -485,
        "source": np.nan,
        "status": "  Won"
    },
    {
        "deal_id": 3002,
        "customer_id": 42,
        "amount": 1200,
        "source": " instagram ",
        "status": "Won"
    },
    {
        "deal_id": 3003,
        "customer_id": 76,
        "amount": np.nan,
        "source": "Facebook",
        "status": "Lost "
    },
    {
        "deal_id": 3004,
        "customer_id": 158,
        "amount": 2500,
        "source": "Telegram",
        "status": np.nan
    },
    {
        "deal_id": 3005,
        "customer_id": 501,                                                     ## Creating problematic data for cleaning
        "amount": 0,
        "source": "Unknown",
        "status": "In Progress"
    },
    {
        "deal_id": 3006,
        "customer_id": 90,
        "amount": 999999,
        "source": "Friend/Relative",
        "status": "Won"
    },
    {
        "deal_id": 3007,
        "customer_id": 42,
        "amount": 1800,
        "source": "Facebook",
        "status": "Won"
    },
    {
        "deal_id": 3007,
        "customer_id": 42,
        "amount": 1800,
        "source": "Facebook",
        "status": "Won"
    }
])

deals = pd.DataFrame(deals)
customers = pd.DataFrame(customers)

deals = pd.concat([deals, deals.iloc[[0]]], ignore_index=True) # Creating duplicate row for cleaning demonstration

deals.to_csv("deals.csv", index = False)
customers.to_csv("customers.csv", index = False)
