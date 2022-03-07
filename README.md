# SRE Assignment

This is simple service that is build in flask python backend framework. It accepts any JSON payload and echos the received payload back to the sender.

## Prerequisites

1. Docker Desktop installed on your machine
2. Kubernetes CLI installed
3. Minikube installed

## Running this app locally

1. Run the following command to build and start the docker containers:
```bash
docker-compose up
```
If there is any error and you need to rebuild the docker images again, run the following command:
```bash
docker-compose up --build
```
2. Open the following url in your browser: http://localhost
3. Send POST http request JSON payload to the endpoint: ../sre

## Deployment

1. Create a minikube cluster
```bash
minikube start
```
2. Deploy to Kubernetes service
```bash
kubectl apply -f deployment.yaml
```
4. Visualize the deployment
```bash
minikube dashboard
```
5. Access the application
```bash
minikube start service: flask-service
```

## Send JSON payload
You may use postman or curl from the terminal to send POST http request to /sre endpoint

## Clean up
```bash
kubectl delete service <service_name>
kubectl delete deployment <deployment_name>
```
Stop Minikube VM (optionally)
```bash
minikube stop
```
Delete Minikube VM (optionally)
```bash
minikube delete
```