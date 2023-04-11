FROM openjdk:11

WORKDIR /app

COPY . /app/

EXPOSE 8080

RUN ./gradlew build

CMD ["java", "-jar", "/app/build/libs/bookshelf-base-server-0.0.1-SNAPSHOT.jar"]