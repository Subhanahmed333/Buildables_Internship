import pandas as pd

df = pd.read_csv("adult.csv")

#!st Task
df.race.value_counts()

#2nd Task
df[df["sex"] == "Male"]["age"].mean()

#3rd Task
percentage_bachelors = (df["education"].value_counts(normalize=True)["Bachelors"]) * 100
percentage_bachelors

#4th Task
advanced_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
filter_with_salary = advanced_education[advanced_education["income"] == ">50K"]
percentage = (filter_with_salary.shape[0] / advanced_education.shape[0]) * 100
print(f"Percentage of advanced-educated people earning >50K: {percentage:.2f}%")

#5th Task
not_advanced_education = df[~df["education"].isin(["Bachelors","Masters","Doctorate"])]
filter_with_salary1 = not_advanced_education[not_advanced_education["income"] == ">50K"]
per_not_advanced = (filter_with_salary1.shape[0] / not_advanced_education.shape[0]) * 100
per_not_advanced

#6th Task
min_hours = df["hours.per.week"].min()
min_hours

#7th Task
people_min_hours = df[df["hours.per.week"] == min_hours]
hours_with_salary = people_min_hours[people_min_hours["income"] == ">50K"]
per_with_hour = (hours_with_salary.shape[0] / people_min_hours.shape[0]) * 100
per_with_hour

#8th Task
country_stats = df.groupby('native.country')['income'].apply(lambda x: (x == '>50K').mean() * 100)
max_country = country_stats.idxmax()
max_percentage = country_stats.max()
print(f"Country: {max_country}")
print(f"Percentage: {max_percentage:.2f}%")

#9th Task
india_high_earners = df[(df['native.country'] == 'India') & (df['income'] == '>50K')]
most_popular_occupation = india_high_earners['occupation'].value_counts().index[0]
print(f"Most popular occupation for >50K earners in India: {most_popular_occupation}")
