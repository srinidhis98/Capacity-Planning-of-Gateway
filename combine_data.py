
from pathlib import Path
from tabulate import tabulate
import sys
import os
import pandas as pd
import plotly.express as px


def combine_data(file1, file2, file3):
    """
    This function is to combined the data from 2 csv files, drops the redundant entries and save it as a new file
    :param file1:
    :param file2:
    :param file3:
    :return:
    """
    data_frame1 = pd.read_csv(file1)
    data_frame2 = pd.read_csv(file2)
    data_frame_out = pd.merge(data_frame1, data_frame2, on="Time", how="outer")
    print(len(data_frame_out))
    print(data_frame_out.head(10))
    drop_duplicate_choice = input("Do you want to drop duplicate items")
    while drop_duplicate_choice.lower() == 'yes':
        try:
            print(data_frame_out.columns)
            drop_items = input('Enter the name of fields separated by space')
            dup_list = drop_items.split()
            print(dup_list)
            df_dup = data_frame_out.drop_duplicates(subset=dup_list, keep="last")
            print(len(df_dup))
            df_dup.to_csv(file3, index=False)
            drop_duplicate_choice = 'no'

        except:
            print('Value Error')
            drop_duplicate_choice = 'yes'

    if drop_duplicate_choice.lower() == 'no':
        data_frame_out.to_csv(file3, index=False)
        print(f'{file3} created')


def data_frame1(args):
    pass


def filter_data(data, file1, column_name):
    """
    This function filters the data and prints it based on the params specified
    :param data:
    :param column_name:
    :param file1:
    :return:
    """
    print(data)
    d_frame = pd.read_csv(file1)
    new_frame1 = tabulate(d_frame.loc[d_frame[column_name] == data], headers= d_frame.loc[
        data == d_frame[column_name]].columns, tablefmt='psql', showindex=False)
    # new_frame2 = d_frame.loc[d_frame[column_name] == data]
    print(new_frame1)
    # print(new_frame2)
    save = input("Need to save as a file [Y/N]: ")
    if save.lower() == 'y':
        output = input('Enter file name with extension:')
        file_open = open(output, 'w')
        file_open.write(new_frame1)
        # file_open.write(new_frame2)

    else:
        pass


def graphs(file, x_co, y_co):
    """
    Displays a basic graph
    :param file:
    :param x_co:
    :param y_co:
    :return:
    """
    dataframe = pd.read_csv(file)
    fig = px.line(dataframe, x=x_co, y=y_co, title=f'{x_co} and {y_co}')
    fig.show()


def main():
    path = Path()
    while True:
        choice = int(input("Enter a Choice\n1. Combine Data\n2. Filter data\n3. Graphs\n4. exit"))
        if choice == 1:

            for file in path.glob('*.csv'):
                print(file)
            file1 = input("Enter file1 to combine")
            file2 = input("Enter file2 to combine")
            file3 = input("Enter the output file")
            # if '.csv' in file1:
            #     print("Yes")
            if '.csv' in file1 and '.csv' in file2 and '.csv' in file3 \
                    and os.path.isfile(file1) \
                    and os.path.isfile(file2):
                combine_data(file1=file1, file2=file2, file3=file3)
            else:
                print("Wrong File names")

        elif choice == 2:

            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file to filter")
            if '.csv' in file_name and os.path.isfile(file_name):
                data_frame = pd.read_csv(file_name)
                print(data_frame.columns)
                col_name = input("Enter the column which is to be filtered")
                data_to_be = input('Enter data to be filtered')
                filter_data(data_to_be, file1=file_name, column_name=col_name)
            else:
                print("Wrong File name")

        elif choice == 3:

            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file for graph")
            if '.csv' in file_name and os.path.isfile(file_name):
                print(pd.read_csv(file_name).columns)
                print("x_axis is taken as Time")
                y_axis = input('Enter y_axis key')
                graphs(file_name, 'Time', y_axis)
            else:
                print("Wrong File name")

        else:
            sys.exit()


if __name__ == '__main__':
    main()
