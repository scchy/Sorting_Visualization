#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy
# Function: 堆排序 HeapSort
# 加载包
from .data import get_data
from .data import get_figure2draw


def big_endian(ds, root, end):
    """
    将堆的末端子节点作调整，使得子节点永远小于父节点  
    :param: ds    get_figure2draw  
    :param: root int 开始（list index）  
    :param: end int 结束（list index）  
    """
    arr = ds.data
    child = root * 2 +  1 # 左子节点
    while child <= end: 
        if child + 1 <= end and arr[child] < arr[child + 1] :
        # 判断右child是否存在，如果存在则和另外一个同级节点进行比较
            child += 1
        if arr[root] < arr[child]:
            ds.swap(root, child)
            ## 下钻到下层
            root = child
            child = root * 2 + 1
        else:
            break

def HeapSort(ds):
    """
    堆排序
    """
    Length = ds.length - 1
    first = Length // 2 
    for root in range(first, -1, -1):
    # 建堆
        big_endian(ds, root, Length)
    for end in range(Length, 0, -1):
        # 堆顶是最大的值，放到最末尾，长度-1后继续建堆
        ds.swap(0, end) 
        big_endian(ds, 0, end - 1) 


if __name__ == "__main__":
    data = get_data(64)
    ds = get_figure2draw(data, sort_title = 'HeapSort')
    ds.Visualize() # 画出底图
    HeapSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
