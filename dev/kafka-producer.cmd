@ECHO OFF

REM docker exec -ti unicauob_kafka1_1 kafka-console-producer --broker-list localhost:9092 --topic ccfraud

call kafka-env.bat
call %KAFKA_HOME%\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic ccfraud


