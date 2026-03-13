import pandas as pd
import numpy as np
import random
import os


np.random.seed(42)

n= 5000

industries = ["Travel","Finance","Technology","Retail","Education","Healthcare"]
subscription_types = ["Basic","Pro","Enterprise"]
payment_status = ["On_time","Late","Failed"]
countries = ["Sri lanka", "USA", "UK", "Australia", "India", "Germany"]


data =[]


for i in range(n):

    industry = random.choice(industries)
    subscription = random.choice(subscription_types)
    country = random.choice(countries)
    
    usage_frequency = np.random.randint(1, 41)
    login_activity = np.random.randint(1, 120)
    support_tickets = np.random.poisson(2)
    monthly_spend = np.random.randint(20, 500)
    payment_history = random.choice(payment_status)

    churn_probability = 0

    if usage_frequency < 5:
        churn_probability += 0.4

    if login_activity < 10:
        churn_probability += 0.3

    if support_tickets > 5:
        churn_probability += 0.2

    if payment_history == "Failed":
        churn_probability += 0.3


    churn = 1 if random.random() < churn_probability else 0

    data.append([
        industry,
        subscription,
        country,
        usage_frequency,
        login_activity,
        support_tickets,
        monthly_spend,
        payment_history,
        churn
    ])

columns = [
    "industry",
    "subscription_type",
    "country",
    "usage_frequency",
    "login_activity",
    "support_tickets",
    "monthly_spend",
    "payment_history",
    "churn"
]

df = pd.DataFrame(data, columns=columns)

# Add some missing values
for col in ["usage_frequency", "login_activity"]:
    df.loc[df.sample(frac=0.02).index, col] = np.nan

os.makedirs("data", exist_ok=True)
df.to_csv("data/churn_dataset.csv", index=False)


print("Dataset generated successfully")