# Installing rook

## ARM images

cyb70289 have created an ARM image for cephcsi, so we are using that for access to the rook storage solution from the different ARM workers. `cyb70289/cephcsi:canary`

A multi architecture image have been created for node-driver-registrar, the source code together with the docker images created (Dockerfile.Amd64, Dockerfile.Arm64, Dockerfile.Arm) can be found in the node-driver-registrar folder.

## Installation

Setup CephFs supporting ReadWriteMany

`kubectl apply -f 01-common.yaml`

`kubectl apply -f 02-operator.yaml`

`kubectl apply -f 03-cluster-test.yaml`

`kubectl apply -f 04-filesystem-test.yaml`

`kubectl apply -f 05-storageclass.yaml`

Setup rbd supporting ReadWriteOnce

`kubectl apply -f 01-common.yaml`

`kubectl apply -f 02-operator.yaml`

`kubectl apply -f 03-cluster-test.yaml`

`kubectl apply -f alternative-04-storageclass.yaml`

