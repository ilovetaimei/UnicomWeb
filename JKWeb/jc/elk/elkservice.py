# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from elasticsearch import Elasticsearch
import time
netedsl={
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "ip": "349"
          }
        },
        {
          "match": {
            "portindex": "7"
          }
        }
      ],
       "filter": {
             "range": { "datatime": { "gte": "2019-01-01 11:00:00", "lte": "2019-01-01 11:00:00" }}
        }


    }
  },
  "aggs":{
        "time":{
            "date_histogram":{
                "field":"datatime",
                "interval":"1h",
                "format":"yyyy-MM-dd HH"
                }

            ,
        "aggs": {
                  "maxinspeed": {"max":       {"field": "inspeed"} },
                  "mininspeed": {"min":       {"field": "inspeed"} },
                  "avginspeed": {"avg":       {"field": "inspeed"} },
                  "maxoutspeed": {"max":       {"field": "outspeed"}},
                  "minoutspeed": {"min":       {"field": "outspeed"}},
                  "avgoutspeed": {"avg":       {"field": "outspeed"}}
              }
        }


 }
}


basepingdsl={
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "ip": "349"
          }
        }
      ],
       "filter": {
             "range": { "datatime": { "gte": "2019-01-01 11:00:00", "lte": "2019-01-01 11:00:00" }}
        }


    }
  },

"aggs":{
    "time": {
        "date_histogram": {
            "field": "datatime",
            "interval": "1h",
            "format": "yyyy-MM-dd HH"
        }

        ,
        "aggs": {
            "maxdelay": {"max": {"field": "maxdelay"}},

            "avgdelay": {"avg": {"field": "avgdelay"}},
            "lostpercent": {"avg": {"field": "lostpercent"}},

        }
    }

}
}
'''
   type :报表类型入hour , day, week, month
   interval ：时间间隔如1h,2h,3h .....;只有type hour 有效
   timerange 00:00-24:00 只有type hour 有效
  
'''
def netdatareport(ip,port,starttime,stoptime,interval):
    localtime = time.localtime(time.time())
    strdateTime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)

    netedsl["query"]["bool"]["must"][0]["match"]["ip"] = ip
    netedsl["query"]["bool"]["must"][1]["match"]["portindex"] = port
    localTime = time.localtime(time.time())
    strdate = time.strftime("%Y-%m-%d ", localTime)

    strmonth = time.strftime("%Y-%m ", localTime)

    netedsl["aggs"]["time"]["date_histogram"]["interval"] = interval
    netedsl["query"]["bool"]["filter"]["range"]["datatime"]["gte"] =starttime
    netedsl["query"]["bool"]["filter"]["range"]["datatime"]["lte"] = stoptime
    if interval=='1M':
        netedsl["aggs"]["time"]["date_histogram"]["format"] = "yyyy-MM"
    else:
        netedsl["aggs"]["time"]["date_histogram"]["format"] = "yyyy-MM-dd HH:mm:ss"

    global es
    rs = es.search(index="netdata", doc_type="netdata", body=netedsl)


    data = []

    for item in rs["aggregations"]["time"]["buckets"]:
        data.append({"avgoutspeed":item["avgoutspeed"]["value"],
         "avginspeed": item["avginspeed"]["value"],
         "maxinspeed": item["maxinspeed"]["value"],
         "mininspeed": item["mininspeed"]["value"],
         "minoutspeed": item["minoutspeed"]["value"],
         "maxoutspeed": item["maxoutspeed"]["value"],
         "time":item["key_as_string"]
         })

    return data


def pingreport(ip,   type):
    localtime = time.localtime(time.time())
    strdateTime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    import copy
    pingdsl=copy.deepcopy(basepingdsl)
    pingdsl["query"]["bool"]["must"][0]["match"]["ip"] = ip

    localTime = time.localtime(time.time())
    strdate = time.strftime("%Y-%m-%d ", localTime)

    strmonth = time.strftime("%Y-%m ", localTime)

    strdatetime=strdate+"00:00:00"
    timestruct = time.strptime(strdatetime, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(timestruct))-604800
    weektime = time.localtime(timestamp)
    strweek = time.strftime("%Y-%m-%d %H:%M:%S", weektime)

    pingdsl["query"]["bool"]["filter"]["range"]["datatime"].pop("lte")
    if type == "day":  # 当天
        pingdsl["aggs"]["time"]["date_histogram"]["interval"] = "1d"
        pingdsl["query"]["bool"]["filter"]["range"]["datatime"]["gte"] = strdate + "00:00:00"

    if type == "week":
        pingdsl["aggs"]["time"]["date_histogram"]["interval"] = "7d"
        pingdsl["query"]["bool"]["filter"]["range"]["datatime"]["gte"] = strweek
        pingdsl["aggs"]["time"]["date_histogram"]["format"] = "yyyy-MM-dd"
    if type == "month":
        pingdsl["aggs"]["time"]["date_histogram"]["interval"] = "1m"
        pingdsl["aggs"]["time"]["date_histogram"]["format"] = "yyyy-MM"
        pingdsl["query"]["bool"]["filter"]["range"]["datatime"]["gte"] = str(localTime.tm_year) + "-01-01 00:00:00"
    global es
    rs = es.search(index="pingdata", doc_type="pingdata", body=pingdsl)


    data = []


    for item in rs["aggregations"]["time"]["buckets"]:
        data.append({"maxdelay": item["maxdelay"]["value"],
                     "avgdelay": item["avgdelay"]["value"],
                     "lostpercent": item["lostpercent"]["value"],

                     "time": item["key_as_string"]
                     })

    return data


def main():

    global es, indexname
    #a=netdatareport("10.7.32.17", "7")
    #print(a)
    a = pingreport("192.168.86.16", "day")
    print(a)
    ''''''
elk = '192.168.87.12'
es = Elasticsearch(elk, ignore=[400, 404])
if __name__ == '__main__':
    main()


indexname = "pingdata"




