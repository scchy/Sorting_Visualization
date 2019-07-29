#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 环排序 CycleSort
# Reference: https://www.cnblogs.com/kkun/archive/2011/11/28/2266559.html

# 加载包 
from .data import get_data
from .data import get_figure2draw

def CycleSort(ds):
    """
    环排序只适用于整数排序，且数正好范围在[0,N-1]内，且只有少量重复元素，不稳定
    """
    assert isinstance(ds, get_figure2draw), "Type Error"
    assert isinstance(ds.data[0], int), "Type Error"

    Length = ds.length
    dt = ds.data
    # 重复元素的列表
    repeatIdxs = []
    for i in range(Length):
        currIdx = i
        # 查找当前值应该所在的索引 
        shouldIdx = sum([1  if dt[currIdx] > v else 0 for v in  dt ])
        # cycle 跑圈 (忽视重复值)
        while currIdx != shouldIdx and dt[currIdx] != dt[shouldIdx]: # 当前位置不是应该所在的位置的时候
            ds.swap(currIdx, shouldIdx) # 交换 currIdx, shouldIdx 的值
            shouldIdx = sum([1 if dt[currIdx] > v else 0 for v in  dt ])
        # 可能包含重复的值记录
        if dt[currIdx] == dt[shouldIdx] and  currIdx != shouldIdx:
            repeatIdxs.append([currIdx, shouldIdx])
    # 重复元素插值
    for rep in repeatIdxs:
        if dt[rep[0]] == dt[rep[1]]:
            ds.set_val(rep[0], dt[max(rep[0] - 1, 0)])

            
if __name__ == "__main__":
    # data = get_data(64)
    data = [51, 8, 46, 18, 40, 20, 14, 33, 5, 10, 62, 48, 53
    , 56, 0, 60, 6, 42, 39, 57, 25, 54, 59, 24, 19, 55, 32, 30
    , 58, 38, 29, 50, 49, 22, 44, 3, 7, 28, 16, 26
    , 41, 52, 4, 23, 35, 31, 36, 43, 61, 17, 37, 13
    , 45, 15, 9, 34, 47, 12, 27, 21, 11, 63, 2, 1, 2, 13, 2, 8]
    ds = get_figure2draw(data, sort_title = 'CycleSort')
    ds.Visualize() # 画出底图
    CycleSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
