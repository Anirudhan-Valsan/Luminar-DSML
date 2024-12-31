def convert_numbers(num_list):
    final_list = []
    for num in num_list:
        new_lst = []
        while num > 0:
            n = num % 1000
            n_str = str(n)
            if len(n_str)<3:
                n_str = '0'*(3-len(n_str))+ n_str
            new_lst.insert(0,n_str)
            num = num // 1000
        if new_lst and new_lst[0].startswith('0'):
            new_lst[0] = new_lst[0].lstrip('0')
        new_num = ','.join(new_lst)
        final_list.append(new_num)
    return final_list

print(convert_numbers([1000000,2356989,2354672,9878098]))












