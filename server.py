import os
import subprocess

test_cmd = 'nc -vz database-1-instance-1.c6ralslvhwx7.us-east-1.rds.amazonaws.com 3306'

process = subprocess.Popen(test_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
err = process.stderr.read()
print str(err)
ans = process.stdout.read()

print str(ans)
