from doctest import OutputChecker
from gettext import find
import random
from re import ASCII
def list_display(list):
    for i in range(0,len(list)):
        print(str(i+1), ". ", str(list[i]))
def random_list (down_range, up_range, list, Number):
    for i in range(0,Number):
        list.append(random.randint(down_range, up_range))
#bool variable is_growing, will sort list from smallest to biggest if its true, if it is false it will sort from biggest to smallest
def list_sort(list, is_growing, Nu):
    a = 0
    sort_count = 0 #to delete it later, only to find out how many times loops will go 
    for i in range(0, Nu-1):
        N = Nu -1
        #if line 15 is commented, then it will be normall bubble sorting
        is_sorted = True
        while N-a > i:
            if (int(is_growing)*2-1)*(list[N][0]) < (int(is_growing)*2-1)*(list[N-1][0]):
                temp = list[N][0]
                list[N][0] = list[N-1][0]
                list[N-1][0] = temp
                temp = list[N][1]
                list[N][1] = list[N-1][1]
                list[N-1][1] = temp
                is_sorted = False
            elif (int(is_growing)*2-1)*(list[N][0]) == (int(is_growing)*2-1)*(list[N-1][0]):
                list.pop(N)
                Nu -=1
                a -= 0
            N -= 1 
            sort_count += 1
        if is_sorted == True:
            break
    #print("counts of how many loop went ", sort_count)
#def find_number works only with sorted list
def find_number(list, element, is_growing):
    i = 0
    j = len(list) -1
    s = -1
    while(j >= i):
        if ((element > list[i][0]) and (element <= list[int((i+j)/2)][0])):
            j = int((i+j)/2)
        else:
            i = int((i+j+1)/2)
    if element == list[j][0]:
        s = list [j][1]
    return s       
def is_list_sort(list, is_growing):
    is_sorted = True
    for N in range (1, len(list)):
        if (int(is_growing)*2-1)*(list[N]) < (int(is_growing)*2-1)*(list[N-1]):
            is_sorted = False
    return is_sorted
#fifo - first in, first out
def fifo (list, head, tail, time, dt_head, dt_tail, list_size):
    while(time<30):
        if(head!=tail):
            list[int(head)] = head
            if(time%dt_tail == 0):
                print(list[tail])
                tail+=1
        if (time%dt_head == 0):
            head += 1 
        if(head >= list_size):
            head = 0
        if (tail >= list_size):
            tail = 0
        time+=1
#lifo - last in, first out
def lifo(list, head, tail, time, dt_head, dt_tail, list_size):
        while(time<20):
            if(head == 0):
                head = 7
            if (tail == 0):
                tail = 7
            if(head!=tail):
                list[int(head)] = head
                if(time%dt_tail == 0):
                    print(list[tail])
                    tail-=1
            if (time%dt_head == 0):
                head -= 1 

            time+=1
time = 0
dt_head = 1
dt_tail = 2
#print("1", "%", "dt_head", 1%dt_head)
#print("3", "%", "dt_tail", 3%dt_tail)
List = [0,1,2,3,4,5,6,7]
list_size = len(List)
head = 7
tail = 0
print("fifo: ")
fifo(List, head, tail, time, dt_head, dt_tail, list_size)
print("\nlifo: ")
lifo(List, head, tail, time, dt_head, dt_tail, list_size)
''''
r_range = 10
n = 100
is_growing = True
Tab = []
for i in range(0, n):
    #in ASCII leters are from 97 to 122
    Tab.append([random.randint(0,r_range), i])
#print(Tab)
list_sort(Tab, is_growing, n)
print("\n")
print(Tab)
#element what index we want to find in our Array
element = 2
print(find_number(Tab, element, is_growing))'''


