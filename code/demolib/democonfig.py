from . import Namespace


kafka_conf_azure = {
    'bootstrap.servers': 'demofraud.servicebus.windows.net:9093', #replace
    'security.protocol': 'SASL_SSL',
    # 'ssl.ca.location': '/path/to/ca-certificate.crt',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'sasl.password': 'Endpoint=sb://demofraud.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=BKs5Ut6ifShxH+LyBOIpRMS1S9LJaP7CG2ckBItzgQE=',
    'client.id': 'ccfraud-demo-producer'
}

kafka_conf_local = {
    'bootstrap.servers': '127.0.0.1:9092',
    'client.id': 'ccfraud-demo-producer'
}

kafka_conf = kafka_conf_local

cfg = Namespace({
    'db': Namespace({
        # 'uri': 'mongodb://demofraud:cFbH1mILM9xN2tMXrY5QZJCixKxgtq60M0XjK3vzZ9z5PUztrJ8CgfAHNCVa5UIqOLOGfBexI8OfxcUJEvuyzA==@demofraud.documents.azure.com:10255/?ssl=true&replicaSet=globaldb',
        'uri': 'mongodb://127.0.0.1',
        'name': 'ccfraud',
        'customer': 'customer',
        'transaction': 'transaction',
        'fraud': 'fraud',
        'nonfraud': 'nonfraud'
    }),
    'load': Namespace({
        'dir': '../data/ccfraud',
        'customer': 'customer.csv',
        'transaction': 'transactions.csv',
        'event_transaction': 'event_transactions.csv'
    }),
        'model': Namespace({
        'preprocessing': Namespace({
            'path': '../data/model/preprocessing'
        }),
        'predict': Namespace({
            'path': '../data/model/predict'
        })
    }),
    'kafka': Namespace({
        'config': kafka_conf,
        'topic': 'ccfraud',
        'groupid': 'ccfraud'
    }),
    'app_name': 'ccFraudDetection',
    'spark_packages': ['org.mongodb.spark:mongo-spark-connector_2.11:2.4.1',
                       'org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4'
                      ],
    'flags_dir': '../flags'
})
