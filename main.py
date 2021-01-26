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
  print(testUnit.query(test1))


def test_sessions():
  '''-- TEST Sessions -- '''
  print("Started Sessions test at {}".format(ctime()))
  testUnit = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  test2 = sessionsQuery("sessions", length=1, expression="ip.dst%3D%3D10.0.0.0%2F8", date_range=720)
  print(test2)
  input()
  print(testUnit.query("sessions"))


if __name__ == "__main__":
  test_fields()
  input()
  test_sessions()
  