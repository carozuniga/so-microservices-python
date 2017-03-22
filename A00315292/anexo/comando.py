from subprocess import Popen, PIPE
import sys
p1=Popen((sys.argv[1]).split(" "), stdout=PIPE)
output=p1.communicate()[0]
print output
