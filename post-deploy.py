#!/usr/local/bin/python3

## Get env_name arg from cli, and use it to determine which env to run against ##

import argparse
import botocore
import boto3

def get_bucket_name(env):
    """ Get the value of bucket_name from the env config file
    by searching for a line containing "bucketName" and assigning
    a value to bucketname
    """

    filename = env + ".cfg"

    for line in open(filename):
        if "bucketName" in line:
            bucket_name = line.split("'")[1]
            print("Bucket Name is: %s" % bucket_name)
            return(bucket_name)
            break

def list_bucket_objects(bucket_name):
    """ List all objects in a bucket"""

    bucket = s3.Bucket(bucket_name)

    objects = bucket.objects.all()
    for object_name in objects:
        print ("Object Name is : %s " % object_name.key)

    return objects

def update_metadata_on_objects(bucket_name, objects):
    """ Update metadata on all objects in a bucket"""

    # Copy Object over itself, setting CacheControl metadata
    for object_name in objects:

        object_content_type = s3.Object(bucket_name, object_name.key).content_type
        s3.Object(bucket_name, object_name.key).copy_from(
            CopySource=bucket_name + "/" + object_name.key,
            CacheControl="public, max-age=300",
            ContentType=object_content_type,
            MetadataDirective="REPLACE"
            )

parser = argparse.ArgumentParser()
parser.add_argument("env", type=str, help="Environment name dev|stage|prod")
args = parser.parse_args()

if args.env == "dev" or args.env == "stage" or args.env == "prod" :
    #print ("Env is " + args.env)
    bucket_name = get_bucket_name(args.env)
    s3 = boto3.resource('s3')
    objects = list_bucket_objects(bucket_name)
    update_metadata_on_objects(bucket_name, objects)
    #put_bucket_object(bucket_name)

else:
    print ("Env has invalid value: " + args.env)
    parser.print_help()

# print trailing crlf
print("")
