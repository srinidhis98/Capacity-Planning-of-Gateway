import sys
import pandas as pd
import numpy as np
from tabulate import tabulate


def print_data(min_df):
    memory_used_percent = float(min_df['Used']) / float(min_df['Total']) * 100
    print("-----------------------------------")
    print('Time: ', min_df['Time'])
    print('CPU core:', min_df['CPU'])
    print('Flow count:', int(min_df['Flow_count']))
    print('Handoff drops:', int(min_df['Handoffq_drops']))
    print('NAT:', min_df['NAT'])
    print('CPU utlised:', float(100 - float(min_df['%idle'])))
    print('Memory Used:', memory_used_percent)
    print('Network Bandwidth[kbps_in/ kbps_out]:', int(min_df['Kbps_in']), '/', int(min_df['Kbps_out']))
    print("-----------------------------------")


def report(data_frame,name):
    sorted_data = remove_na(data_frame)
    min_df = sorted_data.iloc[0]
    print(min_df)
    try:
        print(f'{name}')
        print_data(min_df)
        print(f'CHECK IN \'report.txt\' FOR THIS DETAILS')
        with open('report.txt', 'a') as file:
            sys.stdout = file
            print(f'{name}')
            print_data(min_df)
            sys.stdout = sys.__stdout__

    except ValueError:
        min_df = sorted_data.iloc[1]
        print(min_df)
        print(f'{name}')
        print_data(min_df)
        with open('report.txt', 'a') as file:
            sys.stdout = file
            print_data(min_df)
            sys.stdout = sys.__stdout__


def remove_na(data_frame):
    data_frame = data_frame.replace(r'^\s*$', np.nan, regex=True)
    # print(tabulate(df.head(10), headers=df.columns, showindex=False))
    data_frame = data_frame.sort_values('%idle', ignore_index=True, ascending=True, na_position='last')
    data_frame.fillna(value='-', inplace=True)
    print(tabulate(data_frame.head(10), headers=data_frame.columns, showindex=False, floatfmt='.1f'))

    return data_frame


def main():
    filename = input("enter a filename")
    df = pd.read_csv(filename)
    options ={1:' Overall CPU utilisation', 2:'Core CPU utilisation'}
    choice = input('1. Overall CPU utilisation\n2. Core CPU utilisation')
    if choice == '1':
        df = df.loc[df['CPU'] == ' all']
        print(df.head(10))
        df['NAT'] = df["NAT"].replace(float(0), 'Connection Timed out')
        # print(tabulate(df.head(15), headers=df.columns, tablefmt='psql',floatfmt='.1f'))
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        print(df.columns)
        report(df, name=options[1])

    elif choice == '2':
        df['NAT'] = df["NAT"].replace(float(0), 'Connection Timed out')
        # print(tabulate(df.head(15), headers=df.columns, tablefmt='psql',floatfmt='.1f'))
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        print(df.columns)
        report(df, name=options[2])


if __name__ == '__main__':
    main()