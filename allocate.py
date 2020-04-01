import boto3
import argparse
import time
import os
import re

start_time=time.time()
parser = argparse.ArgumentParser(description='Fast-Flux C2 Emulation')
parser.add_argument('-i', '--instanceId', dest='instanceId', help='EC2 Instance ID')
parser.add_argument('-t', '--time', dest='interval', help='Time interval for associating/releasing elastic ips')
args = parser.parse_args()
ec2 = boto3.client('ec2')
dnsconfig = "/etc/named/zones/db.exploderbot-uah.com"

instance = args.instanceId

while True:
    allocation = ec2.allocate_address(Domain='vpc')
    ec2.associate_address(InstanceId = args.instanceId, AllocationId = allocation["AllocationId"])
    ec2_details = ec2.describe_addresses(Filters=[{'Name': 'instance-id', 'Values': [instance]}])
    for k, v in ec2_details.items():
        if k == 'Addresses':
            addresses = v[0]
            for k, v in addresses.items():
                if k == 'PublicIp':
                    elastic_ip = str(v)
                    with open(dnsconfig, 'r+') as f:
                        a_record = "\n" + "test.exploderbot-uah.com.         IN      A       " + str(v)   
                        f.seek(0, os.SEEK_END)
                        pos = f.tell() - 1
                        while pos > 0 and f.read(1) != "\n":
                            pos -= 1
                            f.seek(pos, os.SEEK_SET)
                        if pos > 0:
                            f.seek(pos, os.SEEK_SET)
                            f.truncate()
                        f.write(a_record)
                    print("Elastic IP Address: " + str(v))
    time.sleep(int(args.interval))
    response = ec2.release_address(AllocationId= allocation["AllocationId"])
    print('Elastic IP Released.')
