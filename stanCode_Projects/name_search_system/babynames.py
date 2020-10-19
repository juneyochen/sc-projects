"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # 建立name_data的dictionary
    # 如果名字不在該dictionary，則把name(附帶year跟rank)加進該dictionary
    if name not in name_data:
        name_data[name] = {year: rank}
    # 如果名子已經在該dictionary裡面，則考慮年分/排名是否要更新
    else:
        if year not in name_data[name]:
            name_data[name][year] = rank
        else:
            if int(name_data[name][year]) > int(rank):
                name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    # 找到記事本檔，讀檔，並把資料存進dictionary裡面
    with open(filename, 'r') as f:
        year = ''  # 把year寫在for loop 外面，這樣else才看的到
        for line in f:
            if len(line) <= 5:       # 年份的字串長度必定比名字的字串長度小(因為年份為19XX，所以我大概抓字串長<=5)
                year = line.strip()  # 把空格刪掉
            else:
                line_list = line.split(',')   # 把每一句用逗號分開
                rank = line_list[0].strip()   # 取出排名
                name1 = line_list[1].strip()  # 男生名字
                add_data_for_name(name_data, year, rank, name1)  # 把名字、年份與排名加到dictionary
                name2 = line_list[2].strip()  # 女生名字
                add_data_for_name(name_data, year, rank, name2)  # 把名字、年份與排名加到dictionary


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    # 把不同的txt檔，寫進name_data這個dictionary裡面
    name_data = {}  # 先建立一個空白字典
    for i in range(len(filenames)):  # 把所有txt讀進去
        add_file(name_data, filenames[i])  # 用上面寫的add_file寫進資料
    return name_data  # return寫好資料的dictionary


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    # 找目標名字，需要注意大小寫問題
    matching_names = []  # 建立一個list，可以記錄找到的名字
    for name in name_data:
        if target.lower() in name.lower():
            matching_names.append(name)  # 找到的話，把它加進一個list
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
