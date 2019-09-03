@ECHO OFF

REM docker exec -ti unicauob_kafka1_1 kafka-topics --bootstrap-server localhost:9092 --list

call kafka-env.bat
call %KAFKA_HOME%\bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --list

pause
