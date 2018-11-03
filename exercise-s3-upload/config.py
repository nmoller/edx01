# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
# in compliance with the License. A copy of the License is located at
#
# https://aws.amazon.com/apache-2-0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"Central configuration"
#import os

import boto3
import json

ssm = boto3.client('ssm', 'us-east-1')

def get_parameter(param_name):
	response = ssm.get_parameters(
		Names=[param_name]
	)
	for parameter in response['Parameters']:
		return parameter['Value']

#####

PHOTOS_BUCKET = get_parameter('edx01_photos_bucket')
FLASK_SECRET = get_parameter('edx01_flask_secret')

# Setup DB
DATABASE_HOST = get_parameter('edx01_db_instance')
DATABASE_USER = get_parameter('edx01_db_user')
DATABASE_PASSWORD = get_parameter('edx01_db_password')
DATABASE_DB_NAME = 'photos'
