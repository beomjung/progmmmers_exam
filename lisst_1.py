array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
answer = []
for command in commands :
    i,j,k = command
    array_list= array[i-1:j]
    array_list.sort()
    middle = array_list[k-1]
    print(middle)
    answer.append(middle)
print(answer)




