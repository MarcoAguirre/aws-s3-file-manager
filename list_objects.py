import argparse
import glob
import logging
import os
import sys


new_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(new_path)

from aws import AWSSession

def main(argv):
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    aws_session = AWSSession()

    parser = argparse.ArgumentParser(description='show list of elements')

    parser.add_argument('bucket', default=None)

    args = parser.parse_args(argv[1:])

    bucket_name = args.bucket
    objects = aws_session.retrieve_obj_list(bucket_name)
    for object in objects:
        logger.info(object['name'])

if __name__ == "__main__":
    sys.exit(main(sys.argv))