from pathlib import Path
import pandas as pd
import os


def main():
    path = Path()
    for file in path.glob('*.txt'):
        print(file)
    filename = input('Enter file name: ')
    if '.txt' in filename and os.path.isfile(filename):
        df = pd.read_csv(filename, sep="|", header=None)
        print(df.head(10))
        if 'flow' in filename:
            header_list = ['Time', 'Flow_count']
            # print(header_list)
            df.columns = header_list
            # print(df.head(10))
            # new_file = input('Enter new file name with .csv extension: ')
            df.to_csv('flow.csv', index=False)

        elif 'handoff' in filename:
            header_list = ['Time', 'Handoffq_drops']
            df.columns = header_list
            df.to_csv('handoff.csv', index=False)

        elif 'mp_modif' in filename:
            header_list = ['Time', 'CPU', '%usr', '%sys', '%idle']
            df.columns = header_list
            df = df[df.CPU != ' ']
            df = df[df.CPU != '   ']
            df.sort_values('Time')
            df.to_csv('mpstat.csv', index=False)

        elif 'mem_modif' in filename:
            header_list = ['Time', 'Total', 'Used', 'Free', 'Shared', 'Buffers', 'Cached']
            df.columns = header_list
            df.to_csv('mem.csv', index=False)

        elif 'nat_modif' in filename:
            header_list = ['Time', 'NAT']
            df.columns = header_list
            df.to_csv('nat.csv', index=False)

        elif 'tun_modif' in filename:
            header_list = ['Time', 'Tunnel_count']
            df.columns = header_list
            df.to_csv('tunnel.csv', index=False)

        elif 'ifstat' in filename:
            header_list = ['Time', 'gwd1_Kbps_in', 'gwd1_Kbps_out', 'eth0_Kbps_in', 'eth0_Kbps_out', 'eth1_Kbps_in',
                           'eth1_Kbps_out', 'eth2_Kbps_in', 'eth2_Kbps_out', 'eth3_Kbps_in', 'eth3_Kbps_out']
            df.columns = header_list
            df.to_csv('ifstat.csv', index=False)


if __name__ == '__main__':
    main()
