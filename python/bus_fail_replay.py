#encoding=utf-8
'''
'''
import re
import urllib2
import time
import string
import thread
import threadpool
import sys,traceback
import logging
import time,random  
total = 0
process_cnt =0
'''
解析xml 返回中的 status 
'''
def getStatus(httpResponseXml):
    pat = re.compile(r"\<why\>(.+?)\<\/why")
    dis1 = pat.findall(httpResponseXml)
    if dis1!=[]:
          dis3 = dis1[0]
          return dis3
    else:
         return  -1
'''
追加时间和状态
'''
def appendStatusAndTime(line):
    print [id, line]
    server_base_url = "http://10.218.76.38:12248"
    fields = line.strip().split(",")
    #print fields
    interval = time.time() 
    try:
        response = urllib2.urlopen(server_base_url.strip()+fields[1].strip(),timeout=10000)
    except Exception:
        print Exception
        traceback.print_exc()
        return
    interval = (time.time() - interval) *1000 
    #print interval
    responseXml=response.read()
    ret = getStatus(responseXml)
    fields.append(ret)
    fields.append(int(interval))
    #print ret; 
    newline = ",".join(str(i) for i in fields)
    return newline
'''

'''
def asyn_callback(request, result): 
    #if process_cnt % 1000 == 0 :
    #print "total : %d --- process " % (total)
    f=open('delay_dist_fail_extend.txt','a+',102400);
    f.write(result + "\r\n")
    f.close()
    if (request.process % 1000) ==0 :
        print "total %20d process %20d  %20f" % (request.total, request.process , request.process/float(request.total)*100) 
 
'''

'''
def main():
    print "=="
    f=open('delay_dist_fail.txt','r',102400);
    lines = f.readlines()
    length = len(lines)
    total = length
    print length
    logging.info("length:%d",length)
    index = 0
    process_cnt=0;
    pool = threadpool.ThreadPool(100)
    for line in lines :
        index +=1;
        logging.info(line)
        process_cnt +=1 ;
        #print line
        requests = threadpool.makeRequests(appendStatusAndTime,[line], asyn_callback) 
        for req in requests:
            req.total = length;
            req.process = process_cnt
            pool.putRequest(req)
        if index == 200:
            pool.wait() 
            index =0
        #print "====="
    pool.wait()        


if __name__ == '__main__':
   main()
