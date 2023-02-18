kubectl delete -f back-deployment.yaml;
kubectl delete -f front-deployment.yaml; 
kubectl delete -f back-service.yaml;
kubectl delete -f front-service.yaml; 

kubectl delete pod --all;
kubectl get pods
kubectl get services


kubectl apply -f back-deployment.yaml
kubectl apply -f front-deployment.yaml

kubectl apply -f back-service.yaml
kubectl apply -f front-service.yaml

echo 'url-front:'
minikube service front-service --url
echo 'url-back:'
minikube service back-service --url
