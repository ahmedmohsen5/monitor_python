import boto3
import schedule 
ec2_client = boto3.client('ec2' , region_name= "us-east-1")
ec2_resources = boto3.resource('ec2' , region_name= "us-east-1")
print('start')


def check_instance_status():
    reservations = ec2_client.describe_instances()
    for reservation in reservations['Reservations']:
        instances = reservation["Instances"]
        for instance in instances:
            print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")
    print('##########################')
        
schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()