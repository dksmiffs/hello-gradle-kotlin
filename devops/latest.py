# -- Read command line args --
# argparse guidance:  https://docs.python.org/3/library/argparse.html
import argparse
parser = argparse.ArgumentParser(description='Update external dependencies.')
parser.add_argument('--verbose', help='chatty output', action='store_true')
args = parser.parse_args()


# -----
import gradle_version
from cd import cd
with cd(".."):
  gradle_version.update(args.verbose)


# -- Update to latest Kotlin version --
# determine existing version

# Use Requests library to track the redirect, guidance here:
# http://docs.python-requests.org/en/master/user/quickstart/#redirection-and-history
import requests
r = requests.get('https://github.com/JetBrains/kotlin/releases/latest')
from urllib.parse import urlparse
o = urlparse(r.url)
from os.path import basename
b = basename(o.path)
# strip off the leading "v"
dontcare, rhs = b.split("v", 1)

if args.verbose:
  print ("latest Kotlin version ==> " + rhs)

