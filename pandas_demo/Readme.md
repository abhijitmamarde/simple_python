# About pandas

- Pandas => Python library for tabular data.
- ETL => Extract Trasform Load
- ETL Pipeline
- Load -> Inspect -> Select -> Filter -> Clean -> Transform -> Group -> Join -> Export

## Install:

```bash
pip install pandas
```

## Import

```python
import pandas as pd
```

## Usage

- Creating DataFrames
- Loading CSV/Excel/JSON
- Selecting and filtering data
- Adding/modifying columns
- Handling missing values
- Sorting
- groupby()
- Merging DataFrames
- Basic aggregation
- Exporting data

# Creating Dataframes

```python
import pandas as pd

data = {
    "name": ["John", "Alice", "Bob"],
    "age": [25, 30, 22],
    "salary": [50000, 70000, 45000]
}

df = pd.DataFrame(data)

print(df)

#     name  age  salary
# 0   John   25   50000
# 1  Alice   30   70000
# 2    Bob   22   45000
```


## Inspect data:

```python

df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

## Dataframe Vs Series

DataFrame -> Rows + Columns -> Table 

Series -> Single Column

## Reading Data

```python
df = pd.read_csv("employees.csv")
df = pd.read_excel("employees.xlsx")
df = pd.read_json("employees.json")
```

## Saving Data

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

## Selecting and Filtering

This is one of the most important Pandas skills.

```python
# Select one column
df["salary"]
# Select multiple columns
df[["name", "salary"]]
# Filter rows
df[df["salary"] > 50000]

# Multiple conditions:

df[
    (df["salary"] > 50000) &
    (df["age"] < 35)
]

# OR:

df[
    (df["salary"] > 70000) |
    (df["age"] < 25)
]

# isin()
df[df["department"].isin(["IT", "HR"])]

# String filtering
df[df["name"].str.startswith("A")]
df[df["name"].str.contains("an")]
```

## Adding & Modifying Columns

```python
# Create a new column:
df["bonus"] = df["salary"] * 0.10

# Create derived column:
df["total"] = df["salary"] + df["bonus"]

# Modify existing column:
df["salary"] = df["salary"] * 1.10

# Modify using apply()
# Prefer vectorized Pandas operations over apply() whenever possible.
df["salary"] = df["salary"].apply(lambda x: x * 1.10)
```

## Handling missing data

```python
data = {
    "name": ["John", "Alice", "Bob"],
    "salary": [50000, None, 45000]
}

df = pd.DataFrame(data)
```

```python
# Find missing values:
df.isna()

# Count them:
df.isna().sum()

# Remove rows:
df.dropna()

# Fill them:
df["salary"] = df["salary"].fillna(0)

# Fill with average:
df["salary"] = df["salary"].fillna(
    df["salary"].mean()
)
```

## Sorting

```python
# Sort by salary:
df.sort_values("salary")

# Sort by salary in descending:
df.sort_values("salary", ascending=False)

# Sort on multiple columns:
df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)
```

## Group By

```csv
name     department    salary
John     IT             50000
Alice    IT             70000
Bob      HR             45000
David    HR             60000
```

```python
# Average salary by department:
df.groupby("department")["salary"].mean()

# Maximum:
df.groupby("department")["salary"].max()

# Minimum:
df.groupby("department")["salary"].min()

# Count:
df.groupby("department")["name"].count()

# Multiple aggregations:
df.groupby("department")["salary"].agg(
    ["mean", "min", "max", "count"]
)
```

Real-world example

```python
sales.groupby("region")["revenue"].sum()
```

Result:

```
North     150000
South     210000
East      180000
West      125000
```

This pattern is worth remembering:

```python
df.groupby("COLUMN")["VALUE_COLUMN"].AGGREGATION()
```

# Merging / Joining DataFrames

Employees

```
employee_id   name
1             John
2             Alice
3             Bob
```

Departments

```
employee_id   department
1             IT
2             HR
3             Finance
```



```python
## Merge
result = pd.merge(
    employees,
    departments,
    on="employee_id"
)

## Inner Join
pd.merge(
    employees,
    departments,
    on="employee_id",
    how="inner"
)

## Left join
pd.merge(
    employees,
    departments,
    on="employee_id",
    how="left"
)
```

# Sample Project

```python
import pandas as pd

data = {
    "name": ["John", "Alice", "Bob", "David", "Eva"],
    "department": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 70000, 60000, 55000, 80000]
}

df = pd.DataFrame(data)

# Find all IT employees
it = df[df["department"] == "IT"]

# Add new col, called bonus, 10% of salary
df["bonus"] = df["salary"] * 0.10

# Find average salary
df["salary"].mean()

# Find average salary by department
df.groupby("department")["salary"].mean()

# Highest paid employee
df.loc[df["salary"].idxmax()]

# sort by salary, descending
df.sort_values("salary", ascending=False)

# Export / save as CSV
df.to_csv("employees_output.csv", index=False)
```