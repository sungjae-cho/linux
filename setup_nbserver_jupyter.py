'''
If notebook does not get connected, it may be that your port is already occupied.
'''
import os
import sys
 
home_dir = os.environ['HOME']

if os.path.isdir("$HOME/.jupyter/jupyter_notebook_config.py")is False:
	os.system('jupyter notebook --generate-config --allow-root')
else: 
    os.system("echo profile_nbserver is already exist.")

from notebook.auth import passwd
pwsha = passwd()
port = input("Port Number (defulat 8888): ")
if port == '':
	port = '8888'

config_str = """
# Server config
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'{}'
# It is a good idea to put it on a known, fixed port
c.NotebookApp.port = {}
c.NotebookApp.notebook_dir = u'{}'
# c.NotebookApp.certfile = u'/opt/certificate/sslcert.pem'
""".format(pwsha, port, home_dir)

with open(home_dir+"/.jupyter/jupyter_notebook_config.py", "w") as cf:
    cf.write(config_str)
        

#os.system("sudo printf \"\nexport PATH=/usr/local/cuda/bin:$PATH\nexport LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH\n\" >> /root/.bashrc")
#os.system("sudo printf \"\nshell -/bin/bash\n\" >> /root/.screenrc")

# this is usually make some error... do not use this!
#os.system("screen -dRR -dmS ipython_notebook ipython notebook --profile=nbserver;")

# https://www.gnu.org/software/screen/manual/screen.html
# screen install check
# 
