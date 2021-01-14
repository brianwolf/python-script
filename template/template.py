#!/usr/bin/env python

"""
Docker build
-----------------------

version 1.0.0
"""

import argparse
import os


# TEMPLATE
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--param", help="un parametro")

args = parser.parse_args()

def create_env_file(name, dict_vars):
    with open(name, "w") as f:
        for k, v in dict_vars.iteritems():
            f.write('{0}={1}\n'.format(k, v))



# SRC
if args.param:
    print("el parametro fue %s" % args.param)

os.system("ls")
create_env_file('result.env', {'param':args.param, 'asd': 'asdasd'})



