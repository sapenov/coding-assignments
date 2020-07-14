i = 'aaabbbccccaa'
o = 'a3b3c4a2'

def frequency_count(a):
    s = set(a) # {a, b, c}
    
    # create a dictionary with frequency counts
    o = {i: a.count(i) for i in s}
    # {a: 3, b: 3, c: 4}
    
    # create it as a string
    str = ""
    for k,v in o.items():
        tmp = k + str(v)
        str += tmp
    
    return str

    
    
    1) Data source (100,000)
    [gps device] > 
    
    Networking:
        LTE (Data throughput, physically)        
    
    Data format:
        parquet
        
    2) HTTP API to acquire data
    
    3) Kafka (intermedaite)
    topic: Toronto 
    
    4) Sink (Business Logic)
    Moving truck: sliding window method to calculate average
    Stopped truck: sessions/ sliding with watermark 10 minutes
    
    5) Store in pesistence
        a) NoSQL db
        b) Data warehouse
        c) AWS S3
        
    6) Data distribution layer
    a) downstream interested in raw
    b) analytical engine (spark cluster) for decision making
    
        
    
