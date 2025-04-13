class SparseArray:
    def __init__(self): #Хранит только НЕ НУЛЕВЫЕ значения индексов
        self.data = {}
    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            del self.data[index]
    def __getitem__(self, index):
        return self.data.get(index, 0) 
if __name__ == "__main__":
    arr = SparseArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))
    arr[10] = 123
    for i in range(8, 13):
        print('arr[{}] = {}'.format(i, arr[i]))
    arr[999999999] = 0
    arr[1000000000] = 123
    print('arr[1000000000] = {}'.format(arr[1000000000]))
