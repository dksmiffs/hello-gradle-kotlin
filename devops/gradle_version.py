def existing():
  from subprocess import check_output
  # shell=True okay in this case, b/c not building the command from user input
  output = check_output("gradlew -v | grep '^Gradle' " + \
                        "| sed 's/^Gradle //'", shell=True, text=True)
  import re
  # eliminate the trailing newline from output, only match the version
  pattern = re.match(r"(.+)", output)
  return pattern.group(1)


def latest():
  import urllib.request
  with urllib.request.urlopen("https://services.gradle.org/versions/current") \
          as url:
    import json
    fullJson = json.loads(url.read().decode())
    # json parsing guidance: https://stackoverflow.com/a/7771071
    return fullJson['version']


def update(verbose=False):
  old = existing()
  new = latest()
  if verbose:
    print("existing Gradle ==> " + old)
    print("latest Gradle   ==> " + new)
  if old == new:
    if verbose:
      print("Gradle update not necessary")
  else:
    # Gradle update guidance:
    #    blog.nishtahir.com/2018/04/15/how-to-properly-update-the-gradle-wrapper
    from subprocess import call
    call("gradlew wrapper --gradle-version " + new + \
         " --distribution-type bin", shell=True)

