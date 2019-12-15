## Setup NFS

### RUN

`kubectl create ns nfs`

`helm install . --name-template nfs --namespace nfs`