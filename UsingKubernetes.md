## Requirements to run in Kubernetes - Minikube:

### Resources:
If you don't have  docker, install using [this](https://docs.docker.com/get-docker/) guide.<br>
If you don't have  minikube, install using [this](https://minikube.sigs.k8s.io/docs/start/) guide.<br>
If you don't have  kubectl, install using [this](https://kubernetes.io/docs/tasks/tools/) guide.

### How to run:
1. Run `git clone https://github.com/gabrielcordeiro2/Hospital-query-system` in terminal.
2. Enter inside project's folder using `cd Hospital-query-system`
3. Create a `.env` file in root project, containing: `DATABASE_URI=postgresql://postgres:123@postgresvc:5432/postgres` and `API_HOST=0.0.0.0`

4. Start Minikube cluster using `minikube start --cpus 4 --memory 8192`
5. Run `minikube addons enable metrics-server`, we need this for autoscaling.
6. Run `kubectl create configmap hospital-api-configmap --from-env-file=.env` for use `.env` variables for the cluster.
7. Run the commands below to build pods and resources for the cluster:
```sh
kubectl apply -f postgres-pvc.yaml
kubectl apply -f postgres-db-deployment.yaml
kubectl apply -f svc-postgres-db.yaml
kubectl apply -f hospital-api-deployment.yaml
kubectl apply -f svc-hospital-api.yaml
kubectl apply -f hospital-api-hpa.yaml
```
8. Run `sh populate_database` in terminal. (If you are in Windows, install Git Bash [here](https://git-scm.com/download/win))
9. (Optional) Just for fun, run `sh stress.sh` in multiple separate terminals to send multiple requests to stress api for autoscaling.
10. (Optional) You can check HPA autoscaling progress by running `kubectl get hpa --watch` or `minikube dashboard`

### Some observations
- You can found my documentation [here](https://documenter.getpostman.com/view/21448782/2s83ziMiKD).
- I have uploaded the application image on [DockerHub](https://hub.docker.com/r/gabrielcordeiro2/hospital-api)
- All endpoint methods, except `/login` needs a JWT Token to use.
- Resources are upcaling every 1 minute.
- Resources are downscaling every 5 minutes.

## Skills that i learned:

- **Database manage**

  Using: PostgreSQL, SQLAlchemy (ORM), Database modeling (ER Diagram).

- **Backend development**
  
  Using: Python, Flask, REST Apis, JWT Auth.

- **Devops**

  Using: Docker, Kubernetes, Shell Script.

- **Rest API Documentation**
  
  Using: Postman and ThunderClient.
  
| ER Database diagram |
|:--:|
|![space-1.jpg](https://user-images.githubusercontent.com/100642061/194748406-81511f29-45a6-4654-af31-9c6cc565457d.png)|
I made this UML diagram using [LucidApp](https://lucid.app/documents#/dashboard).

| Kubernetes cluster diagram |
|:--:|
|![kubernetes-1.jpg](https://github.com/gabrielcordeiro2/Hospital-query-system/assets/100642061/2b9f8a31-111a-4727-b6ba-a49b5e959900)|
I made this UML diagram using [LucidApp](https://lucid.app/documents#/dashboard).



