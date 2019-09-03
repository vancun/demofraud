
from . import cfg, spark

def mongo_read(collection, uri=None, database=None):
    """Create DataFrame from MongoDB collection.
    """
    if uri is None:
        uri = cfg.db.uri
    if database is None:
        database = cfg.db.name
        
    df = spark.read.format("mongo") \
        .option("uri", uri) \
        .option("database", database) \
        .option("collection", collection) \
        .load()
    return df

def mongo_save(df, collection, uri=None, database=None):
    """Update MongoDB collection from DataFrame.
    """
    if uri is None:
        uri = cfg.db.uri
    if database is None:
        database = cfg.db.name
        
    df.write.format("mongo") \
        .option("uri",uri) \
        .option("database", database)  \
        .option("collection", collection) \
        .mode("append") \
        .save()
    return df
