# -- Read command line args --
# argparse guidance:  https://docs.python.org/3/library/argparse.html
import argparse
parser = argparse.ArgumentParser(description='Update external dependencies.')
parser.add_argument('--verbose', help='chatty output', action='store_true')
args = parser.parse_args()


# -- Update to latest Gradle version --
# json from web guidance: https://stackoverflow.com/a/12965254
import urllib.request
with urllib.request.urlopen("https://services.gradle.org/versions/current") \
        as url:
  import json
  fullJson = json.loads(url.read().decode())
  # json parsing guidance: https://stackoverflow.com/a/7771071
  latestVersion = fullJson['version']

  if args.verbose:
    print("latest Gradle version ==> " + latestVersion)

  # Gradle update guidance:
  #    blog.nishtahir.com/2018/04/15/how-to-properly-update-the-gradle-wrapper
  from cd import cd
  with cd(".."):
    from subprocess import call
    call("gradlew wrapper --gradle-version " + latestVersion \
         + " --distribution-type bin", shell=True)


# -- Update to latest Kotlin version --
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

