import datetime
import threading
import sys


def log(headers,log_level,APIname,packagename,msg):
    timestampStr = str(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat())
    thread_id = threading.get_ident()
    sys.stdout.write(timestampStr+"|"+log_level+"|"+str(thread_id)+"|"+"AIP|"+APIname+"|"+packagename+"|"+msg+"\n")
    sys.stdout.flush()    