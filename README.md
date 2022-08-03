# ecr-lifecycle

## About
**ecr-lifecycle** This code manage the lifecycle policy for ECR and it get applied to repository as soon as someone pushes the image to ECR
you can change the policy json file(**lifecyclepolicy.json**)  depending  upon your need..


## Development Setup
1. Clone the repository
   ```
   git clone https://github.com/bharatnainani/ecr-lifecycle.git
   cd ecr-lifecycle
   ```

2. Install serverless framework (may require sudo)
   ```
   npm install -g serverless
   ```
   For more information on how to install srerverless
   Refer [Serverless Installation Documentation](https://www.serverless.com/framework/docs/getting-started#install-as-a-standalone-binary)

3. Install plugins of serverless framework
   ```
   sls plugin install -n serverless-python-requirements
   ```
## Development 
   ```
   sls deploy -s dev 
   ```
