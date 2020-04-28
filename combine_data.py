import pandas as pd
from pathlib import Path


def combine_data(file1, file2, file3):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df_out = pd.merge(df1, df2, on="Time", how="outer")
    print(len(df_out))
    print(df_out.head(10))
    drop_duplicate_choice = input("Do you want to drop duplicate items")
    if drop_duplicate_choice.lower() == 'yes':
        print(df_out.columns)
        drop_items = input('Enter the name of fields separated by space')
        dup_list = drop_items.split()
        print(dup_list)
        df_dup = df_out.drop_duplicates(subset=dup_list, keep="last")
        print(len(df_dup))
        df_dup.to_csv(file3, index=False)
    else:
        df_out.to_csv(file3, index=False)


# def filter_data():
#     file = input("Enter file name to filter")
#     df = pd.read_csv(file)
#     print(df.columns)
#     print(df.dtypes)ye


def main():
    path = Path()
    for file in path.glob('*.csv'):
        print(file)
    f1 = input("Enter file1 to combine")
    f2 = input("Enter file2 to combine")
    f3 = input("Enter the output file")
    combine_data(file1=f1, file2=f2, file3=f3)
    # filter_data()


if __name__ == '__main__':
    main()
