from subprocess import Popen, PIPE

def get_all_users():
  grep_process = Popen(["grep","/bin/bash","/etc/passwd"], stdout=PIPE, stderr=PIPE)
  user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,user_list)

def add_user(username,password):
  add_process = Popen(["sudo","adduser","--password",password,username], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if username in get_all_users() else False

def remove_user(username):
  vip = ["operativos","python","root"]
  if username in vip:
    return True
  else:
    remove_process = Popen(["sudo","userdel","-r",username], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if username in get_all_users() else True

def user_data(username):
 if username in get_all_users():
    grep = Popen (["grep",username,"/etc/passwd"], stdout=PIPE, stderr=PIPE)
    output= grep.communicate()[0]
    return output 
 else:
   
   return False

def recently_logged():
 grep = Popen (["lastlog","-t","1"],stdout=PIPE, stderr=PIPE)
 list = Popen (["awk",'{print $1}'],stdin=grep.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
 return filter(None, list)

def user_commands(username):
 if username in get_all_users():

  list = Popen (["cat","/home/"+username+"/.bash_history"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None, list)
 else:
  return False
