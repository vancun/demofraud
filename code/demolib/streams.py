# See https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#managing-streaming-queries

def streams_stop_all():
    for q in spark.streams.active:
        q.stop()
        print("Query %s stopped" % q.name)
    

def streams_list():
    return list(map(lambda q: q.name, spark.streams.active))
    
__all__ = ['streams_stop_all', 'streams_list']

