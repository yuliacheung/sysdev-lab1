import subprocess

subprocess.Popen("ls", shell=True)
subprocess.Popen(["ls"], shell=False)
subprocess.Popen(
    "echo hi",
    shell=True,
)
subprocess.Popen('echo "a b"', shell=True)
