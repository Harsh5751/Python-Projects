import time
from datetime import datetime as dt

#path of host file; r represent rouge string so things like \n are not interpreted as breakline 
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

#path for testing purposes
hosts_temp_path = "hosts"

#redirect to this ip when blocking websites
redirect = "127.0.0.1"

#lists of websites to block from start time to end time chosen
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

#while keep process running and block websites from 8 am to 4 pm
while True:

    #run from 8 am to 4 pm to block websites
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
       
       #open file to check if list of websites already there; note r+ for read and write(append) modes
        with open(hosts_path, 'r+') as file:
            content = file.read()

            #if website in the file then pass else add it to the file with the redirect
            for website in website_list:
                if(website in content == website):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        print("Work Hours, Facebook and YouTube")

    #delete the websites being blocked in the hosts file after 4pm
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            #set append pointer to top of file instead the end so it will append before the first line
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            #remove everything after the first block or after the last line file write pointer is pointing 
            #works because we are appending before last content not after
            file.truncate()
        print("fun hours")
    time.sleep(5)