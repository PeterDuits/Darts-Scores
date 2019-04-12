#!/usr/bin/env sh

# Sync client files with S3 Bucket
cd fe
echo "Syncing client with S3 Bucket..."
aws s3 sync dist s3://$AWS_WEBSITE_BUCKET/ \
  && echo "Successfully synced client with S3 Bucket."
