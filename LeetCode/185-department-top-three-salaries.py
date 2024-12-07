import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the top 3 salaries for a collection of employees in each department

    Parameters
    ----------
    employee : pd.DataFrame
        keys: id, name, salary, departmentID
    department : pd.DataFrame
        keys: id, name

    Returns
    -------
    df : pd.DataFrame
        keys: Employee, Salary, Department

    Notes
    -----
    My original solution looped over the itertuples in each groupby, incrementing
    a count for each unique value. The groupby DFs were sorted before looping, obviously.
    """
    # rename columns for later use
    employee.rename(columns={"name": "Employee", "salary": "Salary"}, inplace=True)
    department.rename(columns={"name": "Department"}, inplace=True)

    # use GroupBy to compute the ranks
    employee["rank"] = employee.groupby("departmentId")["Salary"].rank(method="dense", ascending=False)

    # extract rows with rank <= 3
    df = employee[employee["rank"] <= 3]

    # merge the department names
    df = df.merge(department, left_on="departmentId", right_on="id", how="inner")
    return df[["Employee", "Salary", "Department"]]
