#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 插入排序 InsertionSort

from .data import get_data
from .data import get_figure2draw

def InsertionSort(ds):
    length = ds.length
    dt = ds.data
    for p in range(length):
        tmp = dt[p]
        i = p
        while i >= 1 and dt[i-1] > tmp:
            # 前一个比较大时
            ds.set_val(i, dt[i-1])
            i -= 1
        ds.set_val(i, tmp)


if __name__ == "__main__":
    data = get_data(100)
    ds = get_figure2draw(data, sort_title = 'InsertionSort')
    ds.Visualize() # 画出底图
    InsertionSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
