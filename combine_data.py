from pathlib import Path
from tabulate import tabulate
import sys
import os
import pandas as pd
import plotly.express as px
import numpy as np


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
            data_frame_out.drop_duplicates(subset=dup_list, keep="first", inplace=True)
            # print(df_dup.head(10))
            # print(df_dup.tail(10))
            # print(len(df_dup))
            print(data_frame_out.tail(10))
            print(len(data_frame_out))
            data_frame_out.to_csv(file3, index=False)
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
    d_frame.sort_values(by='Time', inplace=True)
    new_frame1 = tabulate(d_frame[d_frame[column_name] == data], headers=d_frame[
        d_frame[column_name] == data].columns, tablefmt='psql', showindex=False, floatfmt='.1f')
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
    df = pd.read_csv(file)
    fig = px.line(df, x=x_co, y=y_co, title=f'{x_co} and {y_co}')
    fig.show()


def print_data(min_df):
    row, col = min_df.shape
    new_df = min_df.iloc[0]
    i = 0

    while i <= row:
        if min_df['NAT'].iloc[i] == '-' or min_df['NAT'].iloc[i] == 'nan':
            i += 1
            continue
        elif min_df['Flow_count'].iloc[i] == '-' or min_df['Flow_count'].iloc[i] == 'nan':
            i += 1
            continue
        elif min_df['Handoffq_drops'].iloc[i] == '-' or min_df['Handoffq_drops'].iloc[i] == 'nan':
            i += 1
            continue
        elif min_df['Total'].iloc[i] == '-' or min_df['Total'].iloc[i] == 'nan':
            i += 1
            continue
        elif min_df['Used'].iloc[i] == '-' or min_df['Used'].iloc[i] == 'nan':
            i += 1
            continue
        else:
            new_df = min_df.iloc[i]
            break
    # else:
    #     if float(new_df['NAT']):
    #         new_df['NAT'] = min_df['NAT'].max()
    #     elif float(new_df['Flow_count']):
    #         new_df['Flow_count'] = min_df['Flow_count'].max()
    #     elif float(new_df['Hanodffq_drops']):
    #         new_df['Handoffq_drops'] = min_df['Handoffq_drops'].max()

    memory_used_percent = float(new_df['Used']) / float(new_df['Total']) * 100
    print("-----------------------------------")
    print('Time: ', new_df['Time'])
    print('Flow count:', int(new_df['Flow_count']))
    print('Handoffq drops:', int(new_df['Handoffq_drops']))
    print('NAT:', new_df['NAT'])
    print('Network Bandwidth[kbps_in/ kbps_out]:', int(new_df['eth0_Kbps_in']), '/', int(new_df['eth0_Kbps_out']))
    print('Memory Used:', memory_used_percent)
    print('*Overall* CPU utilised:', float(100 - float(new_df['%idle'])))


def report(data_frame, call):
    if call == 1:
        sorted_data = remove_na(data_frame)
        # min_df = sorted_data.head(10)
        print(tabulate(sorted_data.head(25), headers=sorted_data.columns, tablefmt='psql'))
        # try:
        # print(f'{name}')
        print_data(sorted_data)
        print(f'CHECK IN \'report.txt\' FOR THIS DETAILS')
        with open('report.txt', 'a') as file:
            sys.stdout = file
            # print(f'{name}')
            print_data(sorted_data)
            sys.stdout = sys.__stdout__
        return

    if call == 2:
        core_info = remove_na(data_frame)
        print(tabulate(core_info.head(25), headers=core_info.columns, tablefmt='psql'))
        core_num = core_info['CPU'].iloc[0]
        cpu_util = float(100 - float(core_info['%idle'].iloc[0]))
        print(f'Most loaded CPU utilised: {cpu_util} (core {core_num})')
        print("-----------------------------------")
        with open('report.txt', 'a') as file:
            sys.stdout = file
            print(f'Most loaded CPU utilised: {cpu_util} (core {core_num})')
            print("-----------------------------------")
            sys.stdout = sys.__stdout__
        return
    # except ValueError:
    #     min_df = sorted_data.iloc[1]
    #     print(min_df)
    #     print(f'{name}')
    #     print_data(min_df)
    #     with open('report.txt', 'a') as file:
    #         sys.stdout = file
    #         print_data(min_df)
    #         sys.stdout = sys.__stdout__


def remove_na(data_frame):
    data_frame = data_frame.replace(r'^\s*$', np.nan, regex=True)
    # print(tabulate(df.head(10), headers=df.columns, showindex=False))
    data_frame = data_frame.sort_values('%idle', ignore_index=True, ascending=True, na_position='last')
    data_frame['%idle'] = data_frame['%idle'].astype('float')
    data_frame['%idle'] = data_frame['%idle'].round(3)
    min_val = data_frame['%idle'].min()
    print(min_val)
    data_frame1 = data_frame[data_frame['%idle'] > min_val]
    print(tabulate(data_frame1.head(10), headers=data_frame.columns, showindex=False, floatfmt='.1f'))
    data_frame1.fillna(value='-', inplace=True)
    # print(tabulate(data_frame1.head(10), headers=data_frame.columns, showindex=False, floatfmt='.1f'))
    return data_frame1


def main():
    path = Path()
    while True:
        choice = int(input("Enter a Choice\n1. Combine Data\n2. Filter data\n3. Graphs\n4. Summary\n5. Remove NaN\n6. "
                           "Remove Unnamed\n7. exit"))
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

        elif choice == 4:
            filename = input("enter a filename")
            if '.csv' in filename and os.path.isfile(filename):
                df = pd.read_csv(filename)
                df['NAT'] = df["NAT"].replace(float(0), '-')
                if 'Unnamed: 0' in df.columns:
                    df.drop(columns='Unnamed: 0', inplace=True)
                df = df.loc[df['CPU'] == ' all']
                report(df, call=1)
                df = pd.read_csv(filename)
                df['NAT'] = df["NAT"].replace(float(0), '-')
                if 'Unnamed: 0' in df.columns and 'Unnamed: 0.1' in df.columns:
                    df.drop(columns='Unnamed: 0', inplace=True)
                    df.drop(columns='Unnamed: 0.1', inplace=True)
                df = df.loc[df['CPU'] != ' all']
                report(df, call=2)
            else:
                print('Wrong File name')

        elif choice == 5:
            filename = input("enter a filename")
            if '.csv' in filename and os.path.isfile(filename):
                df = pd.read_csv(filename)
                df = df.replace(np.nan, '-')
                new_file = input('Enter new file name to save')
                df.to_csv(new_file, index=False)
                print(f'{new_file} has been created')

            else:
                print('Wrong File name')

        elif choice == 6:
            filename = input("enter a filename")
            if '.csv' in filename and os.path.isfile(filename):
                df = pd.read_csv(filename)
                if 'Unnamed: 0' in df.columns or 'Unnamed: 0.1' in df.columns:
                    df.drop(columns='Unnamed: 0', inplace=True)
                    df.drop(columns='Unnamed: 0.1', inplace=True)
                    new_file1 = input('Enter new file name to save')
                    df.to_csv(new_file1, index=False)
                    print(f'{new_file1} has been saved with changes')

        elif choice == 7:
            sys.exit()


if __name__ == '__main__':
    main()
