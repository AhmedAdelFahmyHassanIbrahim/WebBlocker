import  time
from datetime import datetime as dt


#declaring variables
hosts_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com" , "facebook.com"]

while True:
    if dt(dt.now().year , dt.now().month , dt.now().day,16) < dt(dt.now().year , dt.now().month , dt.now().day,14):
        print("Working hours .. ")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " +website + "\n")
    else:
        with open(host_path , 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Fun hours ...")


    time.sleep(5)