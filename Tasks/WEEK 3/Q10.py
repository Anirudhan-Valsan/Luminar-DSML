'''
10)Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address
Eg:
Input:
192 168 255 252
Output

192 168 255 253  
192 168 255 254 
192 168 255 255 
192 169 0 0 
192 169 0 1

'''

def next_ip_addresses(octets):
    ip_list = []
    
    for _ in range(5):
       
        octets[3] += 1
        if octets[3] > 255:
            octets[3] = 0
            octets[2] += 1
            if octets[2] > 255:
                octets[2] = 0
                octets[1] += 1
                if octets[1] > 255:
                    octets[1] = 0
                    octets[0] += 1
        ip_list.append(octets[:])
    
    return ip_list


octets = list(map(int, input("Enter the four octets of the IP address separated by spaces: ").split()))

next_ips = next_ip_addresses(octets)


for ip in next_ips:
    print(f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")
