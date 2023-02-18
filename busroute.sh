kubectl delete -f back-deployment.yaml 
kubectl delete -f front-deployment.yaml 
kubectl delete -f service.yaml 

kubectl apply -f back-deployment.yaml
kubectl apply -f front-deployment.yaml

kubectl apply -f service.yaml
minikube service front-back-service --url
