import pandas as pd
import matplotlib.pyplot as plt

# Read the project institutions CSV
df = pd.read_csv("project_institutions.csv")

df = df.sort_values("project_name")

# Add an extra column with the count (number of institutions per project)
df["institution_count"] = df.groupby("project_name")["institution"].transform("count")

df = df[["project_name", "institution_count", "institution"]]

df = df.sort_values("institution_count", ascending=True)

# Save the result to a new CSV
df.to_csv("projects.csv", index=False)

# Do a histogram of the institution counts
dfplot = df[["project_name", "institution_count"]].drop_duplicates()
dfplot["institution_count"].hist()

plt.title("Distribution of Institutions per Project")
plt.xlabel("Number of Institutions in Project")
plt.ylabel("Number of Projects")
plt.tight_layout()
plt.savefig("institutions_per_project_histogram.svg")
plt.close()
