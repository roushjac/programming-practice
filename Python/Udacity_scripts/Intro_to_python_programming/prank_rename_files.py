import os

def rename_files():
    file_list = os.listdir(r'C:\Users\roush\OneDrive\Documents\Python\Udacity_scripts\prank\prank')

    trans_table = {ord(c): '' for c in '1234567890'} # needed for .translate method
    print(trans_table)
    os.chdir(r'C:\Users\roush\OneDrive\Documents\Python\Udacity_scripts\prank\prank')
    for file_name in file_list:
        print('Old name: ',file_name)
        print('New name: ',file_name.translate(trans_table))
        os.rename(file_name, file_name.translate(trans_table))

rename_files()
