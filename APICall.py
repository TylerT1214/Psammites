import sys
sys.path.append("./")
from subprocess import PIPE
from subprocess import Popen
import json

class APICall(object):
  """
  A class built to return data from the Arkime API based on a formatted query.
  
  PARAMETERS
  ----------
  server_address, a string representation of either an IPv4 or resolvable domain name.
  username, the username required to log into the Arkime instance
  password, the password required to log into the Arkime instance

  RETURNS
  ----------
  JSON data converted to a Python dictionary for use.
  """
  def __init__(self, server_address, username, password):
    self.server_address = server_address
    self.username = username
    self.password = password
    

  def query(self, txt):
    request = ("curl -XGET --anyauth -u {}:{} {}/".format(self.username, \
               self.password, self.server_address))
    cmd = str(request + txt)
    data = Popen(cmd.split(), stdout=PIPE)
    response = data.communicate()
    return(response)
  

    

