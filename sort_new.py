from tabulate import tabulate
import sys
import pandas as pd
import numpy as np


def print_data(min_df):
    # tb = sys.exc_info()
    # print(tb)
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
    print('Handoff drops:', int(new_df['Handoffq_drops']))
    print('NAT:', new_df['NAT'])
    print('Network Bandwidth[kbps_in/ kbps_out]:', int(new_df['Kbps_in']), '/', int(new_df['Kbps_out']))
    print('Memory Used:', memory_used_percent)
    print('*Overall* CPU utlised:', float(100 - float(new_df['%idle'])))


def report(data_frame, name):
    if name == 'Overall CPU utilisation':
        sorted_data = remove_na(data_frame, name)
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
    else:
        core_info = remove_na(data_frame, name)
        print(tabulate(core_info.head(25), tablefmt='psql'))
        core_num = core_info['CPU'].iloc[0]
        cpu_util = float(100 - float(core_info['%idle'].iloc[0]))
        print(f'Most loaded CPU utlised: {cpu_util} (core {core_num})')
        print("-----------------------------------")
        with open('report.txt', 'a') as file:
            sys.stdout = file
            print(f'Most loaded CPU utlised: {cpu_util} (core {core_num})')
            print("-----------------------------------")
            sys.stdout = sys.__stdout__

    # except ValueError:
    #     min_df = sorted_data.iloc[1]
    #     print(min_df)
    #     print(f'{name}')
    #     print_data(min_df)
    #     with open('report.txt', 'a') as file:
    #         sys.stdout = file
    #         print_data(min_df)
    #         sys.stdout = sys.__stdout__


def remove_na(data_frame, name):
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
    filename = input("enter a filename")
    df = pd.read_csv(filename)
    options = {1: 'Overall CPU utilisation', 2: 'Core CPU utilisation'}
    choice = input('1. Overall CPU utilisation\n2. Core CPU utilisation')
    if choice == '1':
        df = df.loc[df['CPU'] == ' all']
        # print(df.head(10))
        df['NAT'] = df["NAT"].replace(float(0), '-')
        # print(tabulate(df.head(15), headers=df.columns, tablefmt='psql',floatfmt='.1f'))
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        print(df.columns)
        report(df, name=options[1])

    elif choice == '2':
        df = df.loc[df['CPU'] != ' all']
        df['NAT'] = df["NAT"].replace(float(0), '-')
        # print(tabulate(df.head(15), headers=df.columns, tablefmt='psql',floatfmt='.1f'))
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        print(df.columns)
        report(df, name=options[2])


if __name__ == '__main__':
    main()
