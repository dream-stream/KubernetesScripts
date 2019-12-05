# KubernetesScripts

## Setup Prometheus
Run the following commands:

`cd prometheus`

`kubectl create ns monitoring`

`helm install --namespace monitoring --name-template prometheus-operator --set prometheusOperator.createCustomResource=false -f ./values.yaml  --timeout 10m0s --debug .\charts\stable\prometheus-operator\`

`kubectl apply -f prometheus-service.yaml`

See if the following are needed...

`kubectl apply -f prometheus-monitor.yaml -n monitoring`

`kubectl apply -f service-monitor.yaml`


When creating new deployments/statefulsets be sure to to use the label: **release: prometheus**
And the port should be name and it should be called **web**

## Setup etcd

RPI:

`cd etcd`

`helm install --name-template etcd .` 

Local:

`cd etcd-local`

`helm install --name-template etcd .`

### Commands
`etcdctl get Broker/ --prefix`

`etcdctl get Leader/ --prefix`

`etcdctl get TopicList/ --prefix`

`etcdctl get Topic/ --prefix`

**API documentation:**
https://help.compose.com/docs/etcd-using-etcd3-features


## Setup Zookepper

Go to the Zookeeper folder and read the readme

## Setup Kafka

Go to the Kafka folder and read the readme