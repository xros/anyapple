#!/usr/bin/env python2
# Copyright to Alexander Liu
# LICENCE: FTE v1
"""
                          __________________
                         / ____/_  __/ ____/
                        / /_    / / / __/
                       / __/   / / / /___
                      /_/     /_/ /_____/

                   FREER THAN EVER PUBLIC LICENSE

                        Version 1, March 2016

             Copyright (C) 2016 Alexander Liu <alex(at)nervey.com>

If there exists a most free license, this will be freer than it.
Everyone is permitted to copy, distribute or modifiy anything under this license.

                   FREER THAN EVER PUBLIC LICENSE
    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

0. You are freer than ever to copy, distribute and modifiy anything under this license.
"""

import json
import subprocess
import os



print("[+] Getting all infusions links... ")
# bashCommand = 'curl "https://www.wifipineapple.com/?downloads&list_infusions&mk5"'
bashCommand = 'curl "https://www.wifipineapple.com/modules/mk5/"'
result = subprocess.check_output(bashCommand , shell=True)
the_dict = json.loads(result)


download_links = []

# This works for WifiPineapple mark 5 -- firmware 2.4
download_links_in_types = {}


for name in the_dict:
    mkdir_cmd  = "mkdir -p %s " % name
    result = subprocess.check_output(mkdir_cmd , shell=True)

    # a list to contains all infusions
    download_links_in_types[name] = []
    for i in the_dict[name]:
        print i
        one_link = "http://www.wifipineapple.com/mk5_infusions?infusion=" + i['name'] + "-" + i['version']
        #download_links.append(one_link)
        download_links_in_types[name].append(one_link)

#print(download_links)
#print(download_links_in_types)

print("[+] Trying to download all infusions now... ")
#
# create dir if any
result = subprocess.check_output("mkdir downloads/{cli,sys,usr} -p", shell=True)

for infusion_type in download_links_in_types:
    for link in download_links_in_types[infusion_type]:
        file_name = link.split("=")[1] + ".tar.gz"
        bashCommand = 'wget "' + link + '" -O ./downloads/' + infusion_type + '/' + file_name
        result = subprocess.check_output(bashCommand , shell=True)

print("[+] Finished! All infusions are downloaded. They are in folders: downloads/cli/, downloads/sys/, downloads/usr/ ")

print("[+] Please come here to submit issues https://github.com/xros/anyapple")
