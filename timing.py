import yaml
import requests
import time
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Pass in a .yaml file. See README.md")
        exit()
    try:
        with open(sys.argv[1],'r') as f:
            doc = yaml.safe_load(f)
            for ip in doc['ips']:
                actual_ip = ip.split('@')[1]
                start = time.time()
                try:
                    r = requests.get(actual_ip, timeout=15) # requests is blocking
                except:
                    print("Timeout error @ " + ip)
                    continue
                stop = time.time()
                elapsed = stop - start
                try:
                    print(ip + " " + str(elapsed) + " " + str(r.json()))
                except:
                    print("Error @ " + ip)
    except FileNotFoundError as fnf_error:
            print(fnf_error)
            exit()