import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

file_name = 'omniwebdata_2.lst'
########################################################################################################################################################
def read_data(file_name):
    """
    This function reads in the OMNI data.

    Params:
    ------
    file_name: str or pathlib.Path

    Returns:
    -------
    omni_data:pd.DataFrame
        The DataFrame containing OMNI data with appropriate columns and datetime rows.
    """
    header = parse_header(file_name)
    df = pd.read_csv(file_name, header=None, delim_whitespace=True, names=header, na_values=[99999.9, 9999.99, 999.99])
    
    times = np.nan*np.zeros(df.shape[0], dtype=object)

    for i, row in df.iterrows():
        times[i] = datetime.strptime(f'{int(row[0])} {int(row[1])} {int(row[2])} {int(row[3])}', '%Y %j %H %M')
    
    df.index = times

    return df
########################################################################################################################################################
def parse_header(file_name):
    """
    This function parses the OMNI data header file.

    Params
    ------
    file_name: str or pathlib.Path
        The path to the OMNI data file
    
    Returns
    ------
    header: list
        A list containing the column names 

    """
    file_name = file_name.split('.')[0] + '.fmt'

    header = []

    with open(file_name) as f:

        for _ in range(4):
            next(f)
        
        for row in f:
            header.append(row.split()[1].replace(',', ''))


    return header
########################################################################################################################################################
if __name__ == '__main__':
    df = read_data('omniwebdata_2.lst')

    plt.plot(df.index, df.Speed)
    plt.show()

t = df.index
BX = df.BX
BY = df.BY
BZ = df.BZ
Speed = df.Speed

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)

fig.suptitle('Variables over Time')

ax4.set(xlabel = 'Time')

for ax in (ax1, ax2, ax3, ax4):
    
    if ax != ax4:
        ax.set(ylabel = 'nT')
        
    else:
        ax.set(ylabel = 'km/sec')

ax1.plot(t,BX)

ax1.legend(['Bx GSE, GSM'], loc='upper right')

ax2.plot(t,BY)

ax2.legend(['By GSM'], loc='upper right')

ax3.plot(t,BZ)

ax3.legend(['BZ GSM'], loc='upper right')

ax4.plot(t,Speed)

ax4.legend(['Speed km/sec'], loc='upper right')