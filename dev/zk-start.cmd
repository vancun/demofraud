@ECHO OFF

REM docker-compose -f zk-single-kafka-single.yml up

call kafka-env.bat
call %KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties

