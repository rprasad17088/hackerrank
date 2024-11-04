from collections import Counter

def total_earning(shoe_sizes, shoe_size_price):
    total_earning = 0
    shoe_size_counter = Counter(shoe_sizes)
    for item in shoe_size_price:
        for size in item.keys():
            if size in list(map(int,shoe_size_counter.keys())) and shoe_size_counter[size] > 0:
                total_earning += int(item[size])
                shoe_size_counter[size] -= 1
    return total_earning 


n = int(input())
shoe_sizes = list(map(int,input().split()))
num_customers = int(input())
shoe_size_price = []
for _ in range(num_customers):
    temp_list = input().split()
    shoe_size_price.append({int(temp_list[0]) : int(temp_list[1])})

print(total_earning(shoe_sizes, shoe_size_price))
