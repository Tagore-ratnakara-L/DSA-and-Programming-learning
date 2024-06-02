def List_to_dict():
    keys = [1,2,3]
    values = ['one','two','three']
    result = dict(zip(values,keys))
    print(result)
def dict_to_tuple():
    x = {1: 'one', 2: 'two', 3: 'three'}
    for i in x.items():
        print(i)


if __name__ == '__main__':
    List_to_dict()
    dict_to_tuple()

