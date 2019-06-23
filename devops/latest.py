# -- Read command line args --
# argparse guidance:  https://docs.python.org/3/library/argparse.html
import argparse
parser = argparse.ArgumentParser(description='Update external dependencies.')
parser.add_argument('--verbose', help='chatty output', action='store_true')
args = parser.parse_args()


from devops_spt import Directory, GradleVersion, KotlinVersion
with Directory.cd(".."):
  GradleVersion.update(args.verbose)
  KotlinVersion.update(args.verbose)
