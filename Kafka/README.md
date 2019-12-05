## Kafka


### Build nesseary Kafka arm image
docker build -t dreamstream/kafka:2.3.1-arm ./docker

### Intallation

helm install --name-template kafka ./helm/kafka