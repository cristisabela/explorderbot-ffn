import boto3
import argparse
import time

start_time=time.time()
parser = argparse.ArgumentParser(description='Fast-Flux C2 Emulation')
parser.add_argument('-i', '--instanceId', dest='instanceId', help='EC2 Instance ID')
parser.add_argument('-t', '--time', dest='interval', help='Time interval for associating/releasing elastic ips')
args = parser.parse_args()
ec2 = boto3.client('ec2')

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
                    print("Elastic IP Address: " + str(v))
    time.sleep(int(args.interval))
    response = ec2.release_address(AllocationId= allocation["AllocationId"])
    print('Elastic IP Released.')
