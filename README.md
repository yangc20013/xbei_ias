# xbei_ias

镶贝资讯 demo 

打成jar包
mvn clean package -Dmaven.test.skip=true

启动
java -Dspring.profiles.active=dev -jar target/ias-0.0.1-SNAPSHOT.jar
