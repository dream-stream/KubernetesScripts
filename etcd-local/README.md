Install etcd on local docker cluster:

`helm repo add incubator http://storage.googleapis.com/kubernetes-charts-incubator`

`helm install --name-template etcd incubator/etcd`

Expose etcd on localhost so it can be accessed when running from localhost

`kubectl apply Etcd-Service.yaml` 