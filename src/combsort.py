#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 梳排序 Combsort
# 加载包 
from .data import get_data
from .data import get_figure2draw


def CombSort(ds):
    """
    和气泡排序思路类似  
    该常量为固定值：1.3 (Wlodzimierz Dobosiewicz)
    """
    Length = ds.length
    dt = ds.data
    step = int(Length / 1.3) # 定义步长

    while step:
        for i in range(Length):
            for j in range(i + step, Length, step):
                if dt[ j-step ] > dt[j]: # 逐一比较相邻步数两个值的大小
                    ds.swap(j-step, j) # 交换 j-step, j 的值
        step = int(step / 1.3) # 缩小步长


if __name__ == "__main__":
    data = get_data(64)
    ds = get_figure2draw(data, sort_title = 'CombSort')
    ds.Visualize() # 画出底图
    CombSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
