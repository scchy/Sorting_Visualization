import copy

from .data import DataSeq


def BucketSort(ds):
    """
    桶排序只适用于整数排序，且最大元素不能比数组元素大太多的情况  
    空桶[ 待排数组[ 0 ] ] = 待排数组[ 0 ]
    """
    assert isinstance(ds, DataSeq), "Type Error"
    assert isinstance(ds.data[0], int), "Type Error"

    Length = ds.length
    dt = ds.data
    bucket = [0 for _ in range(max(dt) + 1)]
    for i in range(Length):
        bucket[ dt[i] ] = dt[i] 

    j = 0
    for i in range(Length):
        tmp = bucket[i] 
        while tmp != 'stp': # 有值位置才排序
            ds.SetVal(j , tmp)
            tmp = 'stp'
            j += 1


if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    BucketSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()
