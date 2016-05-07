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

def put_bucket_object(bucket_name):
    """ Put object into S3 bucket, using bucketname from env config file """
    bucket = s3.Bucket(bucket_name)

#    try:
#        s3.meta.client.head_bucket(Bucket=bucket)
#    except botocore.exceptions.ClientError as resp:
#        error_code = int(resp.error_code['Error']['Code'])
#        print("Error accessing bucket : %s, got error code %s" % bucket_name, error_code)
#        exit

    # Upload Object
    #s3.Object(bucket_name, "foo.txt").put(Body=open("./foo.txt", "rb"))

    # Copy Object over itself, setting CacheControl metadata
    object_name = "foo.txt"
    s3.Object( bucket_name, object_name).copy_from(
        CopySource=bucket_name + "/" + object_name,
        CacheControl="public, max-age=300",
        MetadataDirective="REPLACE"
        )

parser = argparse.ArgumentParser()
parser.add_argument("env", type=str, help="Environment name dev|stage|prod")
args = parser.parse_args()

if args.env == "dev" or args.env == "stage" or args.env == "prod" :
    #print ("Env is " + args.env)
    bucket_name = get_bucket_name(args.env)
    s3 = boto3.resource('s3')
    put_bucket_object(bucket_name)
else:
    print ("Env has invalid value: " + args.env)
    parser.print_help()


#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)



# print trailing crlf
print("")
