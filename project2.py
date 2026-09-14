import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

schools = "No of Schools - Total"
boys = "No of Students - Boys"
girls = "No of Students - Girls"
students = "No of Students - Total"
class_x = " PASS PERCENTAGE IN CLASS X - \r\n(Before Compt.) - 2023-24"
class_xii = "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"


#  district has the highest and lowest number of schools?

print(df.loc[df[schools].idxmax(), "District"], df[schools].max())
print(df.loc[df[schools].idxmin(), "District"], df[schools].min())


# district has the highest total student enrollment?

print(df.loc[df[students].idxmax(), "District"], df[students].max())


#  district has the largest gender difference?

df["Gender Difference"] = abs(df[boys] - df[girls])

print(df.loc[df["Gender Difference"].idxmax(), "District"],
      df["Gender Difference"].max())


#  district has the highest Class X pass percentage?

print(df.loc[df[class_x].idxmax(), "District"],
      df[class_x].max())


#  Which district has the highest Class XII pass percentage?

print(df.loc[df[class_xii].idxmax(), "District"],
      df[class_xii].max())


# Compare Class X and Class XII pass percentages across districts.

comparison = df[["District", class_x, class_xii]]

print(comparison)

comparison.plot(
    x="District",
    y=[class_x, class_xii],
    kind="bar",
    figsize=(12, 6)
)

plt.ylabel("Pass Percentage")
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()



# Q8. Does total student enrollment appear to be related to Class X pass percentage?

print(df[students].corr(df[class_x]))

sns.scatterplot(x=df[students], y=df[class_x])

plt.xlabel("Total Students")
plt.ylabel("Class X Pass Percentage")
plt.show()


# Q9. Calculate students per school. Which district has the highest value?

df["Students Per School"] = df[students] / df[schools]

i = df["Students Per School"].idxmax()

print(df.loc[i, "District"])
print(df.loc[i, "Students Per School"])
print(df.loc[i, class_x])

sns.barplot(
    x=df["District"],
    y=df["Students Per School"]
)

plt.xlabel("District")
plt.ylabel("Students Per School")
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()


