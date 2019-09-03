
from .democonfig import cfg

import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName(cfg.app_name) \
    .config('spark.jars.packages', ','.join(cfg.spark_packages)) \
    .getOrCreate()
