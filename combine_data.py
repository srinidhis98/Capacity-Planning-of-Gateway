from pathlib import Path
import sys
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


    else:
        data_frame_out.to_csv(file3, index=False)


def filter_data(*args, file1):
    """
    This function filters the data and prints it based on the params specified
    :param args:
    :param file1:
    :return:
    """

    print(args)
    data_frame1 = pd.read_csv(file1)
    # print(df1.loc[df1['Time'] == args[0]])
    # print(df1.loc[df1['Time'] == args[1]])
    for items in args:
        print(data_frame1.loc[data_frame1['Time'] == items])


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
    while True:
        choice = int(input("Enter a Choice\n1. Combine Data\n2. Filter data\n3. Graphs\n4. exit"))
        if choice == 1:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file1 = input("Enter file1 to combine")
            file2 = input("Enter file2 to combine")
            file3 = input("Enter the output file")
            if file1.count('.csv') == 1 and file2.count('.csv') == 1 and file3.count('.csv') == 1 \
                    and file1 in path.glob('*.csv') \
                    and file2 in path.glob('*.csv'):
                combine_data(file1=file1, file2=file2, file3=file3)
            else:
                print("Wrong File names")

        elif choice == 2:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file to filter")
            # timestamp = input('Enter the timestamp')
            if file_name.count('.csv') == 1 and file_name in path.glob('*.csv'):
                filter_data('3:50:40 AM', '3:50:41 AM', file1=file_name)
            else:
                print("Wrong File name")

        elif choice == 3:
            path = Path()
            for file in path.glob('*.csv'):
                print(file)
            file_name = input("Enter file for graph")
            if file_name.count('.csv') == 1 and file_name in path.glob('*.csv'):
                graphs(file_name, 'Time', 'Flow_count')
            else:
                print("Wrong File name")

        else:
            sys.exit()


if __name__ == '__main__':
    main()
