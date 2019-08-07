#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy
# Function: 堆排序 HeapSort
# 优化 2019-08-07 参考MIT计算机导论 增加交换一次就到下一次
# 加载包
from .data import get_data
from .data import get_figure2draw

def SelectionSort(ds):
    assert isinstance(ds, get_figure2draw), "Type Error"

    Length = ds.length
    for i in range(Length):
        swap_bool = True
        while swap_bool and i < Length - 1: # 优化： 交换一次就停止 
            for j in range(i, Length):
                if ds.data[j] < ds.data[i]:
                    ds.swap(i,j)
                    swap_bool = False



if __name__ == "__main__":
    data = get_data(100)
    ds = get_figure2draw(data, sort_title = 'SelectionSort')
    ds.Visualize() # 画出底图
    SelectionSort(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
    try:
        sys.path.remove(root_path)
    except:
        pass
