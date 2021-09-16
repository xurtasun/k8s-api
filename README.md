# K8S API
### Content
This project contains an application that can be deployed into kubernetes cluster and expose it with an ingress controller.

### Tech stack
```sh
docker
python 3.9.5
k3d
helm
k8s
```
### Requirements

To deploy this project you need to have installed:
- [k3d](https://k3d.io/v4.4.8/#installation)
- [helm](https://helm.sh/docs/intro/install/)

### Project

The goal of this project is to create a minimalistic solution that response some date read from json file. 
Everything was templated with helm `/helm` and parametized with the `values.yaml` file.

### Installation

Once you have installed all the requirements you can run the script `install.sh`.

This will install k3s cluster into your local machine and will expose port `8081` in order to access to ingress controller.

### Resources

This solution creates:
- `deployment`
    - replicaset of `N` pods
- `serviceAccount` with admin permissions (TODO: adjust permissions to once needed)
- `namespace` for all the resources `xurtasun`
- `horizontalAutoscallingGroup` that fix `minPods` in `1` and `maxPods` in `2` depeneding on `% CPU`
- `service` that expose internally the `pods` ports
- simple `ingress` controller that routes trafic to the service

### Test solution

To test the solution yo can simple run `kubectl -n xurtasun get all` to check resources created
After 100 seconds you can request to `http://localhost:8081/data` to receive the data. 
Every request you do will increase the counter of prometheus.

You can check prometheus metrics in `http://localhost:8081/prometheus` and you will see total `requests` done

The response would be a json like `{ hello : world }` with status code 200.

