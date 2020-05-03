import pandas as pd
from pathlib import Path
import plotly.express as px


def combine_data(file1, file2, file3):
    data_frame1 = pd.read_csv(file1)
    data_frame2 = pd.read_csv(file2)
    data_frame_out = pd.merge(data_frame1, data_frame2, on="Time", how="outer")
    print(len(data_frame_out))
    print(data_frame_out.head(10))
    drop_duplicate_choice = input("Do you want to drop duplicate items")
    if drop_duplicate_choice.lower() == 'yes':
        print(data_frame_out.columns)
        drop_items = input('Enter the name of fields separated by space')
        dup_list = drop_items.split()
        print(dup_list)
        df_dup = data_frame_out.drop_duplicates(subset=dup_list, keep="last")
        print(len(df_dup))
        df_dup.to_csv(file3, index=False)
    else:
        data_frame_out.to_csv(file3, index=False)


def filter_data(*args, file1):
    print(args)
    df1 = pd.read_csv(file1)
    # print(df1.loc[df1['Time'] == args[0]])
    # print(df1.loc[df1['Time'] == args[1]])
    for items in args:
        print(df1.loc[df1['Time'] == items])


def graphs(file, x_co, y_co):
    df = pd.read_csv(file)
    fig = px.line(df, x=x_co, y=y_co, title=f'{x_co} and {y_co}')
    fig.show()


def main():
    while True:
        choice = int(input("Enter a Choice\n1. Combine Data\n2. Filter data\n3. Graphs\n4. exit"))
        if choice == 1:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file1 = input("Enter file1 to combine")
            file2 = input("Enter file2 to combine")
            file3 = input("Enter the output file")
            combine_data(file1=file1, file2=file2, file3=file3)

        elif choice == 2:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file to filter")
            # timestamp = input('Enter the timestamp')
            filter_data('3:50:40 AM', '3:50:41 AM', file1=file_name)

        elif choice == 3:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file for graph")
            graphs(file_name, 'Time', 'Flow_count')


        else:
            exit()


if __name__ == '__main__':
    main()
