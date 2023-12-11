import boto3
ec2_client = boto3.client('ec2' , region_name= "us-east-1")
ec2_resources = boto3.resource('ec2' , region_name= "us-east-1")


reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation["Instances"]
    for instance in instances:
        print(instance["ImageId"])
        print(instance["Monitoring"])

