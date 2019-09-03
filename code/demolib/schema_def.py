
from . import Namespace
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, TimestampType


transaction_fields = Namespace({
    'cc_num': 'cc_num',
    'first': 'first',
    'last': 'last',
    'trans_num': 'trans_num',
    'trans_date': 'trans_date',
    'trans_time': 'trans_time',
    'unix_time': 'unix_time',
    'category': 'category',
    'merchant': 'merchant',
    'amt': 'amt',
    'merch_lat': 'merch_lat',
    'merch_long': 'merch_long',
    'distance': 'distance',
    'age': 'age',
    'is_fraud': 'is_fraud',
    'kafka_partition': 'partition',
    'kafka_offset': 'offset'    
})


schema = Namespace()
schema.customer = Namespace()

schema.customer.fields = Namespace({
    'cc_num': 'cc_num',
    'first': 'first',
    'last': 'last',
    'gender': 'gender',
    'street': 'street',
    'city': 'city',
    'state': 'state',
    'zip': 'zip',
    'lat': 'lat',
    'long': 'long',
    'job': 'job',
    'dob': 'dob'
})
customer_fields = schema.customer.fields

schema.customer.schema = StructType([
    StructField(customer_fields.cc_num, StringType(), True),
    StructField(customer_fields.first, StringType(), True),
    StructField(customer_fields.last, StringType(), True),
    StructField(customer_fields.gender, StringType(), True),
    StructField(customer_fields.street, StringType(), True),
    StructField(customer_fields.city, StringType(), True),
    StructField(customer_fields.state, StringType(), True),
    StructField(customer_fields.zip, StringType(), True),
    StructField(customer_fields.lat, DoubleType(), True),
    StructField(customer_fields.long, DoubleType(), True),
    StructField(customer_fields.job, StringType(), True),
    StructField(customer_fields.dob, TimestampType(), True)
])



schema.transaction = Namespace()
source_transaction_fields = ('cc_num', 'first', 'last', 'trans_num', 'trans_date', 'trans_time', 'unix_time', 'category', 'merchant', 'amt', 'merch_lat', 'merch_long', 'is_fraud')
schema.transaction.fields = { k:transaction_fields[k]  for k in source_transaction_fields  }
schema.transaction.schema = StructType([
    StructField(transaction_fields.cc_num, StringType(), True),
    StructField(transaction_fields.first, StringType(), True),
    StructField(transaction_fields.last, StringType(), True),
    StructField(transaction_fields.trans_num, StringType(), True),
    StructField(transaction_fields.trans_date, StringType(), True),
    StructField(transaction_fields.trans_time, StringType(), True),
    StructField(transaction_fields.unix_time, LongType(), True),
    StructField(transaction_fields.category, StringType(), True),
    StructField(transaction_fields.merchant, StringType(), True),
    StructField(transaction_fields.amt, DoubleType(), True),
    StructField(transaction_fields.merch_lat, DoubleType(), True),
    StructField(transaction_fields.merch_long, DoubleType(), True),
    StructField(transaction_fields.is_fraud, DoubleType(), True)
])

"""
schema.event_transaction = Namespace()
event_transaction_fields = ('cc_num', 'first', 'last', 'trans_num', 'trans_date', 'trans_time', 'category', 'merchant', 'amt', 'merch_lat', 'merch_long', 'is_fraud')
schema.event_transaction.fields = { k:transaction_fields[k]  for k in event_transaction_fields  }
schema.event_transaction.schema = StructType([
    StructField(transaction_fields.cc_num, StringType(), True),
    StructField(transaction_fields.first, StringType(), True),
    StructField(transaction_fields.last, StringType(), True),
    StructField(transaction_fields.trans_num, StringType(), True),
    StructField(transaction_fields.trans_date, StringType(), True),
    StructField(transaction_fields.trans_time, TimestampType(), True),
    StructField(transaction_fields.category, StringType(), True),
    StructField(transaction_fields.merchant, StringType(), True),
    StructField(transaction_fields.amt, DoubleType(), True),
    StructField(transaction_fields.merch_lat, DoubleType(), True),
    StructField(transaction_fields.merch_long, DoubleType(), True),
    StructField(transaction_fields.is_fraud, DoubleType(), True)
])

"""
schema.event_transaction = schema.transaction




