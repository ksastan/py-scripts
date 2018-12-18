import os
from ciscoconfparse import CiscoConfParse

def findEthPort(socket, *last_config):
    '''
    parse Cisco config and return interfaces list
    '''
    # extract from tupel -> list
    last_config = last_config[0]
    ports = []
    # run
    for path in last_config:
        parse = CiscoConfParse(path)
        switch = path.split("/")
        serial_objs = parse.find_blocks("description "+socket)
        if serial_objs:
            ports.append('<h4>Switch: ' + switch[3] + '</h4>')
        for obj in serial_objs:
            ports.append(obj)
        serial_objs = []
    return ports


def lastConfig(CONF_DIR, HW_EXCLUSIONS):
    '''
    find last config in each switch folder
    fuction returns list of last config for each switch
    '''
    CONF_DIR_LIST = os.listdir(CONF_DIR, HW_EXCLUSIONS)
    listOfFiles = []  # initialize list
    for directory in CONF_DIR_LIST:
        # skip routers
        if directory in HW_EXCLUSIONS:
            continue
        config_list = os.listdir(CONF_DIR + directory)
        files = [os.path.join(CONF_DIR + directory, file) for file in config_list]
        date_files = [[x, os.path.getctime(x)] for x in files]
        newest_file = sorted(date_files, key=lambda x: x[1], reverse=True)
        if newest_file:
            listOfFiles.append(newest_file[0][0])
    return(listOfFiles)
