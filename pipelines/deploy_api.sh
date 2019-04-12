#!/usr/bin/env sh

aws cloudformation deploy \
    --region ${AWS_DEFAULT_REGION} \
    --template-file build/dist/api-deployment.yml \
    --stack-name ${STACK} \
    --capabilities CAPABILITY_IAM \
    > /dev/null \
    && echo "Package was successfully deployed."

# cd api
# yarn install

# sls config credentials \
#   --provider aws \
#   --key $AWS_ACCESS_KEY_ID \
#   --secret $AWS_SECRET_ACCESS_KEY

# sls decrypt \
#   --stage ${STACK_ENV} \
#   --password ${SERVERLESS_SECRETS_PASS}

# # Deploy serverless stack
# echo "Deploying serverless stack..."
# sls deploy \
#   --stage ${STACK_ENV} \
#   --region ${AWS_DEFAULT_REGION}

# echo "Deployment complete."
