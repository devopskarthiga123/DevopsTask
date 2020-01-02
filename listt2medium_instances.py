#!/usr/bin/env python

import boto3

AWS_ACCESS_KEY_ID = '<Access Key>'
AWS_SECRET_ACCESS_KEY = '<Secret Key>'

ec2 = boto3.resource('ec2')

for instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'instance-type', 'Values': ['t2.medium']}]
)
     print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )
