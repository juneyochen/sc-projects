"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
name: June-Yo, Chen
這個程式，幫助使用者找到名字與年度的排名，並用canvas作圖。
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # 把canvas畫布，根據總共幾年，切割成不同大小。(計算每一個column多寬)
    column_width = (width - (GRAPH_MARGIN_SIZE * 2)) / len(YEARS)
    x_coordinate = column_width * year_index + GRAPH_MARGIN_SIZE
    return int(x_coordinate)  # 回傳x座標


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # 先根據題目，畫出需要的三條線
    # 最上面的線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)
    # 最左邊的線
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    # 最下面的線
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # 計算每個column的寬度
    column_width = (CANVAS_WIDTH - (GRAPH_MARGIN_SIZE*2)) / len(YEARS)
    # 把"年度"貼在canvas的圖上(貼在靠近底下的線那邊)，並把每個年度的column畫出來
    for i in range(len(YEARS)):
        add_x = column_width * i
        canvas.create_line(GRAPH_MARGIN_SIZE + add_x, 0, GRAPH_MARGIN_SIZE + add_x, CANVAS_HEIGHT)
        canvas.create_text(GRAPH_MARGIN_SIZE + add_x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # 計算排名的高度
    rank_height = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000
    # 把名字跟排名貼上canvas，並且要把每個名字的排名用線連起來
    # 把給定的名字list一個一個填進去
    for i in range(len(lookup_names)):
        # 如果名字在name_data裡面，要去找排名跟rank
        if lookup_names[i] in name_data:
            for j in range(len(YEARS)):
                # 先找"名字"與"年份"，因為排名可能跌出前1000名
                name = lookup_names[i]  # 找出名字
                year = str(YEARS[j])    # 找出年份
                if year in name_data[name]:   # 如果year在name的dictionary裡面，去找該年的rank
                    name_d = name_data[name]  # 先找到那個名字的dictionary
                    rank = name_d[year]       # 找到當年的排名
                    x1 = get_x_coordinate(CANVAS_WIDTH, j)  # 找到名字的x座標
                    y1 = int(rank) * rank_height + GRAPH_MARGIN_SIZE  # 找到排名的y座標
                    # 用 create_text 貼上名字+排名
                    canvas.create_text(x1, y1, text=''+str(name) + str(rank), anchor=tkinter.SW, fill=COLORS[i])
                    # 如果有兩點以上，則開始畫線，把相同名字在每年的不同排名連起來
                    if j > 0:
                        year_previous = str(YEARS[j - 1])  # 前一年度
                        if year_previous in name_d:
                            x2 = get_x_coordinate(CANVAS_WIDTH, j - 1)                         # 找前一年的x座標
                            y2 = int(name_d[year_previous]) * rank_height + GRAPH_MARGIN_SIZE  # 找前一年的y座標
                            canvas.create_line(x1, y1, x2, y2, fill=COLORS[i])  # 畫線
                        else:
                            # 如果排名掉出1000名，y 座標則是最底端
                            x2 = get_x_coordinate(CANVAS_WIDTH, j - 1)  # 找前一年的x座標
                            y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE      # 找前一年的y座標
                            canvas.create_line(x1, y1, x2, y2, fill=COLORS[i])  # 畫線

                if year not in name_data[name]:  # 如果該年並沒有在name的dictionary裡面，代表的排名並沒有在前1000名
                    name_d = name_data[name]     # 找該名字的dictionary
                    x1 = get_x_coordinate(CANVAS_WIDTH, j)  # 找x座標
                    y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE    # 找y座標
                    canvas.create_text(x1, y1, text=str(name)+'*', anchor=tkinter.SW, fill=COLORS[i])  # 貼名字標籤
                    if j > 0:  # 如果有兩點以上，則開始畫線
                        year_previous = str(YEARS[j - 1])  # 前一年度
                        if year_previous in name_data[name]:  # 如果前一年的有在名字的dictionary裡面
                            x2 = get_x_coordinate(CANVAS_WIDTH, j - 1)  # 找x座標
                            y2 = int(name_d[year_previous]) * rank_height + GRAPH_MARGIN_SIZE # 找排名的y座標
                            canvas.create_line(x1, y1, x2, y2, fill=COLORS[i])  # 畫線
                        else:  # 如果前一年度，並沒有在名字的dictionary裡面
                            x2 = get_x_coordinate(CANVAS_WIDTH, j - 1)  # 找x座標
                            y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE      # 找y座標
                            canvas.create_line(x1, y1, x2, y2, fill=COLORS[i])  # 畫線


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
