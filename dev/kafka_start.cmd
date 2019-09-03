@ECHO OFF

REM docker-compose -f zk-single-kafka-single.yml up

call kafka-env.bat
call %KAFKA_HOME%\bin\windows\kafka-server-start.bat %KAFKA_HOME%\config\server.properties


