import pandas as pd

data = {
    "name": ["John", "Alice", "Bob", "David", "Eva"],
    "department": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 70000, 60000, 55000, 80000]
}

df = pd.DataFrame(data)

# Find all IT employees
it = df[df["department"] == "IT"]
print("IT Employees are:")
print(it)

# Add new col, called bonus, 10% of salary
df["bonus"] = df["salary"] * 0.10

# Find average salary
print("Average Employee Salary:", df["salary"].mean())

# Find average salary by department
print("Average Employee Salary Department wise:", df.groupby("department")["salary"].mean())

# Highest paid employee
print("Highest paid employee salary:", df.loc[df["salary"].idxmax()])

# sort by salary, descending
df.sort_values("salary", ascending=False, inplace=True)

# Export / save as CSV
df.to_csv("employees_output.csv", index=False)
