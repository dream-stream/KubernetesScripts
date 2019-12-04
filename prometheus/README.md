# prometheus

## Setup Prometheus
Two different dashboards have been setup, one is the prometheus-operator hosted on in the [helm repo](https://github.com/helm/charts/tree/master/stable/prometheus-operator).

The second one which is used as the final monitoring of the system is a modified one called [cluster-monitoring](https://github.com/carlosedp/cluster-monitoring) and can be generated to work specificly with K3s. A few modifications have been done to the yaml files so they are force to be placed on the debian VM. 




## Graphs


### General

sum (rate (container_cpu_usage_seconds_total{pod=~"broker-.*", service="kubelet"}[1m])) by (pod)

sum(container_memory_usage_bytes{pod=~"broker-.*", service="kubelet"}) by (pod)


### Producer

sum(messages_batched)

sum(message_batches_sent{BrokerConnection=~"Topi.*"})

sum(message_batches_sent{BrokerConnection=~"ws.*"})