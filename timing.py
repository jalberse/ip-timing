import yaml

if __name__ == "__main__":
    with open('ips.yaml','r') as f:
        doc = yaml.safe_load(f)
        for ip in doc['ips']:
            # TODO test time for each IP and output
            print(ip)