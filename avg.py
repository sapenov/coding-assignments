def avg_wrd_len(sntc):
    line = sntc.split(" ")
    s = sum(len(w) for w in line)
    avg = s/len(line)
    return avg, int(avg)

sntc = "I would not worry too much about the performance difference between the two approaches as it is marginal. I would really only optimise this if it proved to be the bottleneck in your application which is unlikely."
print(avg_wrd_len(sntc))
