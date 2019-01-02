# -- Read command line args --
# argparse guidance:  https://docs.python.org/3/library/argparse.html
import argparse
parser = argparse.ArgumentParser(description='Update external dependencies.')
parser.add_argument('--verbose', help='chatty output', action='store_true')
args = parser.parse_args()


from cd import cd
with cd(".."):
  import gradle_version
  gradle_version.update(args.verbose)

  import kotlin_version
  kotlin_version.update(args.verbose)

