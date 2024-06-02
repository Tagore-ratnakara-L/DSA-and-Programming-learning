
def Missing_Num_array(num_array):
    print(sum(num_array))
    last_num = num_array[-1]
    Sum=0
    total =(last_num*(last_num+1))//2
    print(total)
    Sum  = sum(num_array)
    print(total-Sum)
    

if __name__ == '__main__':
    num_array = [1,2,4,5,6,7]
    Missing_Num_array(num_array)