## ZooKeeper


### Build nesseary ZooKeeper arm image
docker build -t dreamstream/zookeeper:3.5.6-arm .\docker\

### Intallation

helm install --name-template zookeeper ./helm/zookeeper