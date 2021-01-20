import json
import sys
sys.path.append('./Testing/Generic')
sys.path.append('./Testing/v3.x')
from time import ctime
from APICall import APICall
from sessionsQuery import sessionsQuery


if __name__ == "__main__":
  print("Started at {}".format(ctime()))
  testUnit = APICall('https://demo.arkime.com', 'arkime', 'arkime')

  test2 = sessionsQuery("sessions", length=1, expression="ip.dst%3D%3D10.0.0.0%2F8", date_range=720)
  #print(test2)
  #input()
  #print(testUnit.query(test1))
  data = json.loads(testUnit.query(test2)[0])
  data_list = data['data']
  print(data.keys())
  for entry in data_list:
    print(entry.keys())