#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 桶排序 BucketSort
# 加载包  
import copy
from .data import get_data
from .data import get_figure2draw


def BucketSort(ds):
    """
    桶排序只适用于整数排序，且最大元素不能比数值元素大太多
    空桶[ 待排数组[ 0 ] ] = 待排数组[ 0 ]
    """
    assert isinstance(ds, get_figure2draw), "Type Error"
    assert isinstance(ds.data[0], int), "Type Error"

    Lengh = ds.length
    dt = ds.data
    bucket = [0 for _ in range(max(dt) + 1)]
    for i in range(Lengh):
        bucket[ dt[i] ] = dt[i] 

    j = 0
    for i in range(Lengh):
        tmp = bucket[i] 
        while tmp != 'stp': # 有值位置才排序
            ds.set_val(j , tmp)
            tmp = 'stp'
            j += 1

if __name__ == "__main__":
    data = get_data(64)
    ds = get_figure2draw(data, sort_title = 'BucketSort')
    ds.Visualize() # 画出底图
    BucketSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
