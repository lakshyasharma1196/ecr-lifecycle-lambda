import os
import json
import boto3
 
def ecr_lifecycle(lifecycle_policy):
    ecr_client = boto3.client('ecr')

    repositories = []
    describe_repo_paginator = ecr_client.get_paginator('describe_repositories')
    for response_list_repopaginator in describe_repo_paginator.paginate():
        for repo in response_list_repopaginator['repositories']:
            repositories.append(repo['repositoryName'])
    for repository in repositories:
        response = ecr_client.put_lifecycle_policy(repositoryName=repository,lifecyclePolicyText=json.dumps(lifecycle_policy))
    return response


def lambda_handler(event, context):
    path = os.path.dirname(__file__) 
    json_file = open(os.path.join(path, 'lifecyclepolicy.json'))
    data = json.load(json_file)
    ecr_lifecycle(data)
    