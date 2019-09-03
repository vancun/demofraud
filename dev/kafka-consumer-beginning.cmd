@ECHO OFF
REM docker exec -ti unicauob_kafka1_1 kafka-console-consumer --bootstrap-server localhost:9092 --topic ccfraud --from-beginning

call kafka-env.bat
call %KAFKA_HOME%\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic ccfraud --from-beginning


