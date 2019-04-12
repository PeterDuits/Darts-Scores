#!/usr/bin/env sh

# prepare build directory
rm -rf build && mkdir -p build/dist

# copy root into build dir
rsync --exclude-from pipelines/exclude.txt -avz ./api/ ./build/dist/

# install pip dependencies in build dir
cd api
pipenv install --deploy
rsync --exclude-from ../pipelines/exclude.txt -avz $(pipenv --venv)/lib/python3.6/site-packages/ ../build/dist/

# build sam template
echo "Executing ansible playbook..."
cd ../cloudformation/ansible/${CI_ENVIRONMENT_NAME}
ansible-playbook build-api.yml

# upload cloudformation package
echo "Packaging cloudformation..."
aws cloudformation package \
    --template-file ../../../build/dist/api-template.yml \
    --s3-bucket ${AWS_UPLOAD_BUCKET} \
    --output-template-file ../../../build/dist/api-deployment.yml \
    > /dev/null \
    && echo "API package was successfully built."
