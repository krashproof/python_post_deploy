#!/usr/local/bin/python3

## Get env_name arg from cli, and use it to determine which env to sun against ##

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("env", type=str, help="Environment name dev|stage|prod")
args = parser.parse_args()

if args.env == "dev" or args.env == "stage" or args.env == "prod" :
    print ("Env is " + args.env)
else:
    print ("Env has invalid value: " + args.env)
    parser.print_help()

print("")

