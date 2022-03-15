import random
def list_display(list):
    for i in range(0,len(list)):
        print(str(i+1), ". ", str(List[i]))
def random_list (down_range, up_range, list, Number):
    for i in range(0,Number):
        list.append(random.randint(down_range, up_range))
#bool variable is_growing, will sort list from smallest to biggest if its true, if it is false it will sort from biggest to smallest
def list_sort(list, is_growing):
    Nu = len(list)
    sort_count = 0 #to delete it later, only to find out how many times loops will go 
    for i in range(1, Nu):
        N = Nu - 1
        while N > 0:
            if (int(is_growing)*2-1)*(List[N]) < (int(is_growing)*2-1)*(List[N-1]):
                temp = List[N]
                List[N] = List[N-1]
                List[N-1] = temp
            N -= 1  
def is_list_sort(list, is_growing):
    is_sorted = True
    for N in range (1, len(list)):
        if (int(is_growing)*2-1)*(List[N]) < (int(is_growing)*2-1)*(List[N-1]):
            is_sorted = False
    return is_sorted
#setting list size and deciding if we wnat to sort it later from smallest to biggest or from biggest to smallest;
Number = 50
is_growing = False
List = []
print("Lets draw", Number, " numbers from 0 to 20:")
random_list(0, 20, List, Number)
list_display(List)
print("\nnow we can sort list with our drawn numbers :")
if is_list_sort(List, is_growing) == False:
    list_sort(List, is_growing)
#display sorted list
list_display(List)
#print(is_list_sort(List, is_growing))
