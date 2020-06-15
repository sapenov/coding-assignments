# convert number to hex

def conv_to_hex(n):
    if n == 0:
        return 0

    def helper_func(num, acc):
        if num == 0:
            return acc
        else:
            quot = num//16
            rem = num%16
            acc.insert(0, rem)
            # print(f"acc is {acc}, num is {num}, quot is {quot}, rem is {rem}")
            return helper_func(quot, acc)

    def helper_func_v2(num, acc):
        if num == 0:
            return acc
        else:
            qr = divmod(n, 16)
            acc.insert(0, qr[1])
            return helper_func(qr[0], acc)

    def format_num(arr):
        return sum(d*10**i for i, d in enumerate(arr[::-1]))


    #h = helper_func(n, [])
    h = helper_func_v2(n, [])
    fh = format_num(h)


    return h, fh

# driver code

print(conv_to_hex(1128))
print(conv_to_hex(0))



