'''
Tyler Teegardin 
CMSC 495
2/28/2021
'''
#pip install psutil, & pip install -U kaleido
import plotly.graph_objects as go
import sys
sys.path.append('./')
import datetime
from APICall import APICall
from sessionsQuery import sessionsQuery

#PPS function to retrieve services info.
def pps(ip, direction, stop, start, conn):
  #Establishing connection and query syntax.
  #conn = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  if stop == None or start == None:
    syntax = sessionsQuery("unique", \
    exp = "port.dst", \
    counts = 1, \
    expression="ip.src%3D%3D" + ip, \
    date_range = -1)
  else:
    syntax = sessionsQuery("unique", \
    exp = "port.dst", \
    counts = 1, \
    expression="ip.src%3D%3D" + ip, \
    stopTime=stop, \
    startTime=start)
  query = conn.query(syntax)
  #Decoding received binary data to string format.
  qdec = query.decode("utf-8")
  qdecsplit = qdec.split("\n")
  qdecsplit.pop()
  ppsSubDict = {}
  ppsDict = {ip:ppsSubDict}
  #Building dictionary return value containing queried data.
  for val in qdecsplit:
    portName = ''
    f = open("/etc/services",'r')
    port = val.split(",")
    if port[0] == '0':
      portName = 'icmp'
    for line in f:
      lineSplit = line.split()
      for index in lineSplit:
        if port[0] in index:
          if index == port[0] + "/tcp":
            for x in lineSplit:
              if x == '#':
                i = lineSplit.index(x) + 1
                for num in range(i,len(lineSplit)):
                  portName += lineSplit[num] + ' '
    if portName == '':
      portName = 'Port ' + port[0]
    ppsSubDict[portName] = port
    f.close()
  return ppsDict

#Statistics function to build candlestick graph and display statistical info.
def stats(ip,direction,stop,start,conn):
  #Local variable initialization.
  srcIPList = []
  srcBytes = []
  srcPackets = []
  dstIPList = []
  dstBytes = []
  dstPackets = []
  sessionLen = 0
  #Establishing connection.
  if stop == None or start == None:
    syntax = sessionsQuery("sessions", \
    expression="ip." + direction + "%20%3D%3D%20" + ip, \
    date_range = -1)
  else:
    syntax = sessionsQuery("sessions", \
    expression="ip." + direction + "%20%3D%3D%20" + ip, \
    stopTime=stop, \
    startTime=start)
  query = conn.query(syntax)
  data = query.get("data")
  numSessions = len(data)
  if numSessions == 0:
    errResponse(syntax)
  else:
    try:
      #Parsing data retrieved from each session.
      for i in range(numSessions):
        dStats = data[i]
        sessionLen += dStats.get("lastPacket")-dStats.get("firstPacket")
        if dStats.get("srcIp") not in srcIPList:
          srcIPList.append(dStats.get("srcIp"))
          srcBytes.append(dStats.get("srcBytes"))
          srcPackets.append(dStats.get("srcPackets"))
        else:
          index = srcIPList.index(dStats.get("srcIp"))
          srcBytes[index] += dStats.get("srcBytes")
          srcPackets[index] += dStats.get("srcPackets")
        if dStats.get("dstIp") not in dstIPList:
          dstIPList.append(dStats.get("dstIp"))
          dstBytes.append(dStats.get("dstBytes"))
          dstPackets.append(dStats.get("dstPackets"))
        else:
          index = dstIPList.index(dStats.get("dstIp"))
          dstBytes[index] += dStats.get("dstBytes")
          dstPackets[index] += dStats.get("dstPackets")
      
      #Beginning of building candlestick graph
      byt = []
      statDict = {}
      count = 0
      passedPorts = []
      portDataRange = []
      timeList = []
      #Building dictionary and some lists.
      for val in data:
        statDict[count] = [val.get("dstPort"),val.get("totBytes")]
        lPack = val.get("lastPacket")
        fPack = val.get("firstPacket")
        timeDelt = int((lPack - fPack) / 2)
        newTime = (timeDelt + fPack) / 1000.0
        fixTime = datetime.datetime.fromtimestamp(newTime).strftime('%Y-%m-%d %H:%M:%S.%f')
        timeList.append(fixTime)
        count += 1
      #Building rest of lists.
      for key in statDict:
        tempLi = []
        li = statDict[key]
        if li[0] not in passedPorts:
          if li[0] <= 1024:
            passedPorts.append(li[0])
            byt.append(li[1])
            tempLi.append(li[1])
            portDataRange.append(tempLi)
        else:
          if li[0] <= 1024:
            ind = passedPorts.index(li[0])
            tempLi.append(li[1])
            portDataRange[ind].append(li[1])
            byt[ind] += li[1]
      #Refining lists to create graph.
      openVal = []
      closeVal = []
      highVal = []
      lowVal = []
      sortedPortData = []
      for pData in portDataRange:
        sortedPortData.append(sorted(pData))
      for sData in sortedPortData:
        lenVal = len(sData) - 1
        openVal.append(sData[0])
        closeVal.append(sData[lenVal])
        if len(sData) % 2 == 0:
          mid = int((len(sData)/2) - 1)
          lowVal.append(sData[mid])
          highVal.append(sData[mid+1])
        else:
          mid = int(len(sData)/2 - 0.5)
          lowVal.append(sData[mid])
          highVal.append(sData[mid])
      maxByt = 0
      #Try except block to catch data which has no data transfer on dstByte field.
      try:
        maxByt = int(max(byt))
      except ValueError:
        print("No bytes were transferred by the destination. Graph could not be made.")
      #Creating graph figure and saving it as .png
      fig = go.Figure(data=[go.Candlestick(x=passedPorts,
                       open=openVal, high=highVal,
                       low=lowVal, close=closeVal)])
      fig.update_layout(xaxis_rangeslider_visible=False)
      fig.update_layout(yaxis_range=[0,maxByt])
      #fig.write_image("test.png") #Remove
      #fig.show()
      return fig
    except IndexError:
      errResponse(syntax)

#Generic Error Response   
def errResponse(syntax):
  print("\nYou received 0 results with the query " + "\"" + syntax + "\".")

#Main
if __name__ == "__main__":
  conn = APICall('https://demo.arkime.com', 'arkime', 'arkime')
  stats("170.116.176.223", "src", None, None, conn)
  