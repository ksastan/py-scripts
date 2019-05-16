# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return(x*fact(x-1))
# print(fact(5))

def sum(arr):
        if len(arr) == 1:
                return(arr[0])
        elif len(arr) == 0:
                return(0)
        else:
                arr[0] += arr.pop()
                sum(arr)
a = 1
def elements(arr, b=1):
        if len(arr) == 1:
                print('Len = %s' % len(arr))
                print('List elements count = %s' % b)
        elif len(arr) == 0:
                return 0
        else:
                arr.pop()
                b += 1
                print('From else ' + str(b))
                elements(arr, b)
print(elements([1,2,3]))

def quick_sort(array):
        if len(array) < 2:
                return(array)
                