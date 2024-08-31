import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


table = pd.read_csv("test.csv")
table = table.sample(n=1000, replace=False)

table.fillna(0)
table = table.loc[table["Rooms"] > 0]

plt.hist(table["Rooms"], bins=4, ec="black")
plt.title("Гистограмма")
plt.xlabel("Rooms")
plt.ylabel("Quantity")
plt.show()

# sns.boxplot(data=table, x='Rooms', y='LifeSquare', whis=0.5)
#
# plt.xlabel('Rooms')
# plt.ylabel('Price')
# plt.title('График с усами')
# plt.show()

print(table.groupby("Rooms").agg({"Rooms": "count"}), "\n")


print(table.pivot_table(values="Id", index=["DistrictId"], columns=["Rooms"], aggfunc="count", fill_value=0))

table.to_csv("surname.csv")
