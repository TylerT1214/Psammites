import json
import sys
sys.path.append('./')
from time import ctime
from APICall import APICall
from sessionsQuery import sessionsQuery


def test_fields():
  '''-- TEST Fields -- '''
  print("Started Fields test at {}".format(ctime()))
  testUnit = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  test1 = sessionsQuery("fields")
  data = testUnit.query(test1)
  print(type(data))
  input()
  print(data)
  input()
  print("Total fields: ", len(data.keys()), "\n")
  for key in data.keys():
    print(key, data[key])
    input()  


def test_sessions():
  '''-- TEST Sessions -- '''
  print("Started Sessions test at {}".format(ctime()))
  testUnit = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  test2 = sessionsQuery("sessions", \
  expression="ip.src%20%3D%3D%2091.198.120.253", \
  stopTime=1637437258, \
  startTime=892446679)
  print(test2)
  input()
  print(testUnit.query(test2))


if __name__ == "__main__":
  #test_fields()
  #input()
  test_sessions()
  