from shell.bash import execute

result = execute("20.125.63.183","free -g")
print (result)

result = execute("20.125.63.183",'ps aux|grep "python"')
print (result)