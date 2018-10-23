# xbei_ias

镶贝资讯 demo 

打成jar包
mvn clean package -Dmaven.test.skip=true

启动
java -Dspring.profiles.active=dev -jar target/ias-0.0.1-SNAPSHOT.jar

-Dspring.datasource.url="jdbc:mysql://localhost:3306/xbei_ias?useUnicode=true&characterEncoding=UTF-8" -Dspring.datasource.user
name="root" -Dspring.datasource.password='root' -Dserver.port=8080
