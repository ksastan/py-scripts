import psutil

def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9.8 Kb'
    >>> bytes2human(100001221)
    '95.4 Mb'
    """
    symbols = ('Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f' % (n)

def mem_use():
    """
     memory usage
    """
    mem = psutil.virtual_memory()
    print("Available memory is", bytes2human(mem.available))

def disk_use():
    '''
    show disk usage for all systems disks
    '''
    disk_path = psutil.disk_partitions()
    for i in disk_path:
        print("Disk %s usage is %s percent" % (i[0], psutil.disk_usage(i[1])[3]))

def net_use():
    '''
    show network usage and errors
    '''
    net_use = psutil.net_io_counters(pernic=True)
    for interf in net_use:
        print("-"*10 + interf + "-"*40)
        print("Sent %s" % bytes2human(net_use[interf][0]))
        print("Receive %s" % bytes2human(net_use[interf][1]))
        print("Errors %s" % net_use[interf][4])
