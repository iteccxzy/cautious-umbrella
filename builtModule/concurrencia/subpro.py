import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "print('HOLA MUNDO')"])


# subprocess.run('dir /A', shell=True)

result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)

print(result.stdout)


subprocess.Popen("start excel", shell=True)