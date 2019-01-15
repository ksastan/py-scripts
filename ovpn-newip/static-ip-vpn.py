#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse
import shutil
import os.path
import os

# path to vpn, change it if you need
global lastip_path
lastip_path = '<path to folder with lastip files>'


def createParser():
    '''
    It could be terminal arguments parser
    '''
    # parser = argparse.ArgumentParser()
    # return parser


def backup(access_type, protocol):
    '''
    backed up existed lastip files
    '''
    shutil.copyfile(lastip_path + '_' + access_type + '_' + protocol,
        lastip_path + '_' + access_type + '_' + protocol + '.bak')


def fileexist(etoken, vpn_path):
    '''
    check ccd folder and stop execution if file exist
    '''
    if os.path.exists(vpn_path + etoken):
        print('File ' + vpn_path + etoken + ' already exist!')
        print('----execution stopped----')
        sys.exit()


def readIP(last_file, access_type, protocol):
    '''
    get last ip from lastip file and return increased ip
    '''
    last_file = lastip_path + '_' + access_type + '_' + protocol
    f = open(last_file, 'r')
    last = f.readline()
    last = last.split(' ')
    ip = last[1]
    gw = last[2]
    # increase ip and gw address
    ip = ip.split('.')
    gw = gw.split('.')
    # check if subnet run out
    if int(ip[3]) + 4 > 254:
        ip[2] = str(int(ip[2]) + 1)
        ip[3] = '2'
        gw[2] = str(int(gw[2]) + 1)
        gw[3] = '1'
    else:
        ip[3] = str(int(ip[3]) + 4)
        gw[3] = str(int(gw[3]) + 4)

    # concatenate ip from list to one string
    ip = '.'.join(ip)
    gw = '.'.join(gw)
    f.close()
    # return incresed string with IP and GW
    return last[0] + ' ' + ip + ' ' + gw


def createFile(etoken, vpn_static_ip, vpn_path, access_type, protocol):
    '''
    create vpn file with vpn_static_ip string
    '''
    new_token = open(vpn_path + etoken, 'w')
    new_token.write(vpn_static_ip + '\n')
    new_token.close()
    os.chown(vpn_path + etoken, 1000, 0)
    os.chmod(vpn_path + etoken, 0644)
    # update lastip.txt with string vpn_static_ip
    new_token = open(lastip_path + '_' + access_type + '_' + protocol, 'w')
    new_token.write(vpn_static_ip)
    new_token.close()


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    # ## check for config exists, make backup, create config file for tcp
    # path where need to create etoken config file
    vpnpath = '/etc/openvpn/ccd-tcp/'
    # it should be first function
    fileexist(namespace.eTokenName, vpnpath)
    # backup file with last used ip
    backup(namespace.type, 'tcp')
    # read file with last ip, generate and return new string
    last_ip_string = readIP(lastip_path, namespace.type, 'tcp')
    # create config file in OpenVPN path with next free ip, update lastip.txt
    createFile(namespace.eTokenName, last_ip_string, vpnpath, namespace.type, 'tcp')
    print('Config file for tcp connection created:')
    print(namespace.eTokenName + ': ' + last_ip_string + '\n')

    # ## check for config exists, make backup, create config file for tcp
    # path where need to create etoken config file
    vpnpath = '/etc/openvpn/ccd-udp/'
    # it should be first function
    fileexist(namespace.eTokenName, vpnpath)
    # backup file with last used ip
    backup(namespace.type, 'udp')
    # read file with last ip, generate and return new string
    last_ip_string = readIP(lastip_path, namespace.type, 'udp')
    # create config file in OpenVPN path with second free ip, update lastip.txt
    createFile(namespace.eTokenName, last_ip_string, vpnpath, namespace.type, 'udp')
    print('Config file for udp connection created:')
    print(namespace.eTokenName + ': ' + last_ip_string + '\n')
