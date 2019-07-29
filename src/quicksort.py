#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 快速排序 quicksort
# 加载包 
from .data import get_data
from .data import get_figure2draw


def Get_midIdx_value(ds, Left, Right):
    """
    三平均分区法改进  
    保证  dt[Left] < dt[Mid] < dt[Right]
    """
    dt = ds.data
    Mid = (Left + Right) // 2
    if dt[Left] > dt[Right]: # 左边大于右边时
        ds.swap(Left, Right)
    if dt[Left] > dt[Mid]:   # 左边大于中间时
        ds.swap(Left, Mid)
    if dt[Mid] > dt[Right]:  # 中间大于右边时
        ds.swap(Mid, Right)
    ds.swap(Mid, Right - 1) # 将中间位置的值 放到 Right的左边
    return dt[Right - 1] # 返回中间位置的值

def Qsort(ds, Left, Right):
    Cutoff = 10
    dt = ds.data
    if Cutoff <= Right-Left:
        MidIdx_vlaue = Get_midIdx_value(ds, Left, Right)
        low = Left + 1
        high = Right - 2
        
        while True:
            while dt[low] < MidIdx_vlaue : # 向后搜索第一个大于 MidIdx_vlaue 的值的位置
                low += 1
            while dt[high] > MidIdx_vlaue: # 向前搜索第一个小于 MidIdx_vlaue 的值的位置
                high -= 1
        
            if low < high: # 
                ds.swap(low, high)
                # 用于进行下一轮查找
                low += 1
                high-= 1
            else:
                break
        ds.swap(low, Right-1) # 将第一个大于 MidIdx_vlaue 的值 和 中间值交换
        Qsort(ds, Left, low - 1)
        Qsort(ds, low + 1, Right)

    else:
        # 元素太少， 用插入排序
        for p in range(Left,Right+1):
            tmp = dt[p]
            i=p
            while i >= 1 and dt[i-1] > tmp:
                ds.set_val(i, dt[i-1])
                i-=1
            ds.set_val(i, tmp)

def QuickSort(ds):
    assert isinstance(ds, get_figure2draw), "Type Error"
    Length = ds.length
    Qsort(ds, 0, Length-1)


if __name__ == "__main__":
    data = get_data(64)
    ds = get_figure2draw(data, sort_title = 'quicksort')
    ds.Visualize() # 画出底图
    QuickSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
