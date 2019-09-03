
from pyspark.sql.functions import *
from .functions import *

udf_dist = udf(earth_distance)

def udf_age(start_date="dob", end_date=None):
    if end_date is None:
        end_date = current_date()
    if isinstance(start_date, str):
        start_dadte = col(start_date)
    return (months_between(end_date,start_dadte)/12).cast("int")

import math


