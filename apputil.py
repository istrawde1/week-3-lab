import pandas as pd


# Exercise 1

def fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 2

def to_binary(n):
    """Return the binary representation of an integer."""
    if n == 0:
        return "0"
    return to_binary(n // 2) + str(n % 2)


# Exercise 3

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)


def task_1():
    """Return column names sorted by missing values."""
    df_bellevue["gender"] = (
        df_bellevue["gender"]
        .replace({"g": pd.NA, "h": pd.NA, "?": pd.NA})
    )
    print("Replaced invalid gender values with missing values.")
    return list(df_bellevue.isna().sum().sort_values().index)


def task_2():
    """Return total admissions by year."""
    df_bellevue["date_in"] = pd.to_datetime(df_bellevue["date_in"])
    date_in_year = df_bellevue["date_in"].dt.year
    return (
        date_in_year.value_counts()
        .reset_index()
        .rename(
            columns={"date_in": "year", "count": "total_admissions"}
        )
        .sort_values("year")
    )


def task_3():
    """Return the average age for each gender."""
    df_bellevue["gender"] = (
        df_bellevue["gender"]
        .replace({"g": pd.NA, "h": pd.NA, "?": pd.NA})
    )
    print("Replaced invalid gender values with missing values.")
    return df_bellevue.groupby("gender")["age"].mean()


def task_4():
    """Return the 5 most common professions."""
    return list(df_bellevue["profession"].value_counts().head(5).index)

