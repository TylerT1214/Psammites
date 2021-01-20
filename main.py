import sys
sys.path.append('./Testing/Generic')
sys.path.append('./Testing/v3.x')
from APICall import *
from sessionsQuery import *
from fields import get_fields

if __name__ == "__main__":
  testUnit = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  #print(type(testUnit))
  queryString = sessionsQuery()[:-1]
  #print(queryString)
  data, _ = (testUnit.query(get_fields()))
  data = json.loads(data)
  print(type(data))
  print (data.keys())