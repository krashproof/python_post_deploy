#!/usr/local/bin/python3

## Get env_name arg from cli, and use it to determine which env to run against ##

import argparse

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

parser = argparse.ArgumentParser()
parser.add_argument("env", type=str, help="Environment name dev|stage|prod")
args = parser.parse_args()

if args.env == "dev" or args.env == "stage" or args.env == "prod" :
    #print ("Env is " + args.env)
    get_bucket_name(args.env)
else:
    print ("Env has invalid value: " + args.env)
    parser.print_help()

# print trailing crlf
print("")

