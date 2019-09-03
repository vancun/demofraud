from .spark import spark

# See https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#managing-streaming-queries

def streams_stop_all():
    for q in spark.streams.active:
        q.stop()
        print(f"Query {q.name} stopped")
    

def streams_list():
    return list(map(lambda q: q.name, spark.streams.active))
    
__all__ = ['streams_stop_all', 'streams_list']

