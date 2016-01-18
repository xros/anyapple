import json
import subprocess


print("[ Getting all infusions links... ]")
bashCommand = 'curl "https://www.wifipineapple.com/?downloads&list_infusions&mk5"'
result = subprocess.check_output(bashCommand , shell=True)
the_dict = json.loads(result)


download_links = []



for name in the_dict:
    for i in the_dict[name]:
        one_link = "http://www.wifipineapple.com/mk5_infusions?infusion=" + i['name'] + "-" + i['version']
        download_links.append(one_link)

#print(download_links)

print("[ Trying to download all infusions now... ]")

for link in download_links:
    file_name = link.split("=")[1] + ".tar.gz"
    bashCommand = 'wget "' + link + '" -O ' + file_name
    result = subprocess.check_output(bashCommand , shell=True)

print("[ Finished! All infusions are downloaded. ]")
