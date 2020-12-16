def triple_list_in_place(int_list):
    for i in range(len(int_list)):
        int_list[i] *= 3
        


def triple_list_out_of_place(int_list):
    
    tripled_list = [None] * len(int_list)
    
    for i in range(len(int_list)):
        tripled_list[i] = int_list[i] * 3
        
    return tripled_list


num_list = [1, 2, 3, 4, 5]
print(num_list)

# triple_list_in_place(num_list)
# print(num_list)

new_list = triple_list_out_of_place(num_list)
print(num_list)