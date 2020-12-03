import os
import subprocess
import sys
import twint
import time

fileIn = sys.argv[1]
fileOut = sys.argv[2]

conf = twint.Config
conf.User_full = True
conf.Store_csv = True
conf.Output = fileOut

index = 0
with open(fileIn, 'r') as user_list:
    for user in user_list:
        user = str.strip(user)
        conf.Username = user
        try:
            twint.run.Lookup(conf)
        except KeyError:
            print(f'unable to pull user {user}')
            continue
        except ValueError:
            print(f'unable to pull user {user}')
            continue
        except RuntimeError as e:
            if (str(e) == 'Not found'):
                print(f'unable to pull user {user}')
                continue
            else:
                servers = ['us6698', 'us6983', 'us8041', 'us8195', 'us8029', 'us8056']
                cmd = ['openpyn', 'us', '-s', servers[index], '-k', '--tcp']
                index = (index+1) % 6
                subprocess.Popen(cmd)
                time.sleep(20)
                conf.Proxy_host = 'localhost' # set twint to new vpn IP
                continue
