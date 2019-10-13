# KubernetesScripts

## Setup Prometheus
Run the following commands:

`kubectl create ns monitoring`

`helm install --namespace monitoring --name-template prometheus --set grafana.service.type=LoadBalancer --set grafana.service.port=3000 --set prometheus.service.type=LoadBalancer stable/prometheus-operator`

`kubectl apply -f prometheus-monitor.yaml -n monitoring`

`kubectl apply -f service-monitor.yaml`


When creating new deployments/statefulsets be sure to to use the label: **release: prometheus**
And the port should be name and it should be called **web**

## Setup etcd

`helm install --name-template etcd incubator/etcd`

### Commands
`etcdctl get Broker/ --prefix`

`etcdctl get Leader/ --prefix`

`etcdctl get TopicList/ --prefix`

`etcdctl get Topic/ --prefix`

**API documentation:**
https://help.compose.com/docs/etcd-using-etcd3-features