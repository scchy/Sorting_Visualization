#！ python 3.6
# Create Date: 2019-06-19
# Author: Scc_hy 
# Function: 冒泡排序 Bubblesort

from .data import get_data
from .data import get_figure2draw


def Bubblesort(ds):
    """
    气泡排序
    """
    # isinstance(object, classinfo) 可以是直接或间接类名
    assert isinstance(ds, get_figure2draw), "Type Error"

    Length = ds.length  
    dt = ds.data
    for i in range(Length-1, -1, -1): # 倒序
        for j in range(0, i, 1): # 顺序
            if dt[j] > dt[j+1]: # 逐一比较相邻两个值的大小
                ds.swap(j, j+1) # 交换 idx1, idx2 的值


if __name__ == "__main__":
    data = get_data(64)
    ds = get_figure2draw(data, sort_title = 'Bubblesort')
    ds.Visualize() # 画出底图
    Bubblesort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
