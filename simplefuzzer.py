import requests
#import urllib3
#http = urllib3.PoolManager()

def subdomain(target):
        #target = "google.com"
    print("Here are the results:\n")
    with open("testfile.txt","r") as f:
    #print(f.readlines())
         for i in f.readlines():
        #print(i.strip())
            s="https://"+i.strip()+"."+target
        #r = http.request('GET', s)
            try:
                r = requests.get(url=s)
                if(r.status_code==200 or r.status_code==301 or r.status_code==302):
                    with open("subdomains.txt","a") as f1:
                            s=s+"\n"
                            f1.write(s)
                    print(s.strip()+" Status Code: "+str(r.status_code))
            except:
                pass  

def directory(target):
        #target = "google.com"
    print("Here are the results:\n")
    with open("testfile.txt","r") as f:
            for i in f.readlines():
                s="https://"+target+"/"+i.strip()
                try:
                    r = requests.get(url=s)
                    if(r.status_code==200 or r.status_code==301 or r.status_code==302):
                        with open("directories.txt","a") as f2:
                            s=s+"\n"
                            f2.write(s)
                        print(s.strip()+" Status Code: "+str(r.status_code))
                except:
                    pass
                 
def main():
    target=input("\nEnter Target (example: abc.com) :\n--> ")
    while(True):
        print("\nEnter 1 for Subdomains")
        print("Enter 2 for Directories")
        print("Enter 0 for Exit")
        n=int(input("\nEnter the Choice:"))
        if(n==1):
            subdomain(target)
        elif(n==2):
            directory(target)
        elif(n==0):
            exit()
        else:
            print("Not A Valid Choice!")
        

if __name__=="__main__":
    main()



