#!/usr/bin/env python2
# Copyright to Alexander Liu, all rights reserved
# LICENCE: GPL V3
import json
import subprocess


print("[+] Getting all infusions links... ")
bashCommand = 'curl "https://www.wifipineapple.com/?downloads&list_infusions&mk5"'
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

for infusion_type in download_links_in_types:
    for link in download_links_in_types[infusion_type]:
        file_name = link.split("=")[1] + ".tar.gz"
        bashCommand = 'wget "' + link + '" -O ./' + infusion_type + '/' + file_name
        result = subprocess.check_output(bashCommand , shell=True)

print("[!] Finished! All infusions are downloaded. They are in folders: cli/, sys/, usr/ ")
