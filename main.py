from src.my_data import get_data
from src.my_data import get_figure2draw
from src.Scc_Bubblesort import Bubblesort
from src.Scc_BucketSort import BucketSort
from src.Scc_Combsort import CombSort
from src.Scc_Cyclesort import CycleSort
from src.Scc_HeapSort import HeapSort
from src.Scc_insertionsort import InsertionSort
from src.Scc_Quicksort import QuickSort

import argparse

def parse_args():
    parser=argparse.ArgumentParser(description="Sort Visulization")
    parser.add_argument('-l','--length',type=int,default=64)
    parser.add_argument('-i','--interval',type=int,default=1)
    parser.add_argument('-t','--sort-type',type=str,default='Bubblesort', 
                                        choices=["Bubblesort","BucketSort","CombSort",
                                                "CycleSort","HeapSort","InsertionSort",
                                                "QuickSort"])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    MAXLENGTH = 1000
    Length     = args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval   = args.interval
    SortType   = args.sort_type

    try:
        SortMethod=eval(SortType) # 将文本转为函数
    except: 
        print("Sort Type Not Found! Please Check if %s Exists or Not!"%SortType)
        exit()

    data = get_data(Length)
    ds = get_figure2draw(data, time_interval=Interval
                             , sort_title = SortType)

    ds.Visualize() # 画出底图
    SortMethod(ds)
    ds.set_time_interval(0)
    ds.Visualize() # 画出排序结束后的图
