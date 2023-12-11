import boto3

ec2_client_paris = boto3.client('ec2' , region_name= "us-east-1" )
ec2_resource_paris = boto3.resource('ec2' , region_name= "us-east-1")

reservations_paris = ec2_client_paris.describe_instances()['Reservations']

instance_id_paris=[]

for res in reservations_paris:
    instance= res['Instances']
    for ins in instance:
        instance_id_paris.append(ins['InstanceId'])
        
        
response = ec2_resource_paris.create_tags(
    Resources=instance_id_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

