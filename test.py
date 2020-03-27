import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
        InstanceIds=['i-0db5586fa02054271'])
print(response)
