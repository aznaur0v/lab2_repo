arr=[3,8,6,2,17,29,1,4,87]
arr1=[5,9,8,11,32]
def poisk_min(template_arr):
    i=0
    min=template_arr[i]
    for i in range(len(template_arr)):
        if template_arr[i]<min:
            min=template_arr[i]
        else:
            pass
    return min

def poisk_sr(template_arr):
    sr=0
    sum=0
    i=0
    for i in range(len(template_arr)):
        sum=sum+template_arr[i]
    sr=sum/len(template_arr)
    return sr

def poisk_sr_2(template_arr):
    for i in range(len(template_arr)):
        sr=int(sum(template_arr)/len(template_arr))
    print("Сумма элементов массива:",sum(template_arr))
    print ("Количество элементов в массиве:",len(template_arr))
    return sr

print("Минимум массива:",poisk_min(arr))
print("-------------------------------------------")
print("Минимум массива:",poisk_min(arr1))
print("-------------------------------------------")
print("Минимум массива(через встроенную функцию min):",min(arr))
print("-------------------------------------------")
print("Среднее арифметическое в массиве:",poisk_sr(arr))
print("-------------------------------------------")
print("Среднее арифметическое в массиве:",poisk_sr_2(arr))
print("-------------------------------------------")
print("Среднее арифметическое в массиве:",poisk_sr(arr1))
print("-------------------------------------------")
print("Среднее арифметическое в массиве:",poisk_sr_2(arr1))


