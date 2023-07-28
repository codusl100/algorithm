N = int(input())
number_str_list = list(map(int, input().split()))
budget = int(input())

def binary(start, end):
    while start <= end :
        mid = (start + end) // 2
        total = 0 
        for i in number_str_list :
            if i > mid :
                total += mid
            else :
                total += i
        if total <= budget :
            start = mid + 1
        else :
            end = mid - 1
    return end

print(binary(0, max(number_str_list)))  