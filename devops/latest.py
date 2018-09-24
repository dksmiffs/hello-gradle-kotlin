from cd import cd
from subprocess import call

import json
import urllib.request

# json from web guidance: https://stackoverflow.com/a/12965254
with urllib.request.urlopen("https://services.gradle.org/versions/current") \
        as url:
  data = json.loads(url.read().decode())
  # json parsing guidance: https://stackoverflow.com/a/7771071
  currentGradle = data['version']
  # Gradle update guidance:
  #    blog.nishtahir.com/2018/04/15/how-to-properly-update-the-gradle-wrapper
  with cd(".."):
    call("gradlew wrapper --gradle-version " + (data['version']) \
         + " --distribution-type bin", shell=True)

