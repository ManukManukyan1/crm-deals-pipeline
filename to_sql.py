# from sqlalchemy import create_engine
# import pandas as pd

# deals_clean = pd.read_csv("deals_clean.csv")
# customers = pd.read_csv("customers.csv")

# engine = create_engine(
#     "postgresql+psycopg://postgres:197348625m@localhost:5432/crm"
# )

# deals_clean.to_sql(
#     name = "deals",
#     con = engine,
#     if_exists = "replace",
#     index = False
# )
# customers.to_sql(
#     name = "customers",
#     con = engine,
#     if_exists = "replace",
#     index = False
# )



# print("Data uploaded successfully!")



import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

deals_clean = pd.read_csv("deals_clean.csv")
customers = pd.read_csv("customers.csv")

engine = create_engine(os.environ["DATABASE_URL"])

deals_clean.to_sql(name="deals", con=engine, if_exists="replace", index=False)
customers.to_sql(name="customers", con=engine, if_exists="replace", index=False)

print("Data uploaded successfully!")