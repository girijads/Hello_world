import subprocess

def execute(server,command):
    command = f'''ssh app@{server} "{command}" '''
    res = subprocess.Popen(command,shell=True)
    res.wait()
    return res.stdout
