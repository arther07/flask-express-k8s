# 🚀 Flask Frontend + Express Backend Deployment on Minikube (Kubernetes)

This project demonstrates how to deploy a **Flask frontend** and an **Express.js backend** in a local **Kubernetes cluster** using **Minikube**. The application showcases a simple todo list functionality with the Flask frontend communicating with the Express.js backend.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Python 3.x](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/)

## 📁 Project Structure

```
flask-express-k8s/
│
├── flask-frontend/
│   ├── app.py                 # Flask application code
│   ├── Dockerfile            # Frontend container configuration
│   └── requirements.txt      # Python dependencies
│
├── express-backend/
│   ├── index.js             # Express application code
│   ├── Dockerfile           # Backend container configuration
│   └── package.json         # Node.js dependencies
│
├── k8s/
│   ├── flask-deployment.yaml    # Frontend deployment configuration
│   ├── flask-service.yaml       # Frontend service configuration
│   ├── express-deployment.yaml  # Backend deployment configuration
│   └── express-service.yaml     # Backend service configuration
│
└── README.md
```

## ⚙️ Technologies Used

- **Frontend**: Python (Flask) - A lightweight WSGI web application framework
- **Backend**: Node.js (Express) - Fast, unopinionated web framework
- **Containerization**: Docker - Platform for developing, shipping, and running applications
- **Orchestration**: Kubernetes - Container orchestration platform
- **Local Cluster**: Minikube - Local Kubernetes cluster

## 🚀 Deployment Guide

### 1. Start Minikube
```bash
# Start Minikube cluster
minikube start

# Verify the cluster is running
minikube status
```

### 2. Configure Docker Environment
```bash
# Configure Docker to use Minikube's Docker daemon
eval $(minikube docker-env)      # For Unix-based systems
minikube docker-env | Invoke-Expression  # For Windows PowerShell
```

### 3. Build Docker Images
```bash
# Build frontend image
docker build -t flask-frontend:latest ./flask-frontend

# Build backend image
docker build -t express-backend:latest ./express-backend

# Verify images are created
docker images
```

### 4. Deploy to Kubernetes
```bash
# Apply Kubernetes configurations
kubectl apply -f k8s/express-deployment.yaml
kubectl apply -f k8s/express-service.yaml
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml

# Verify deployments and services
kubectl get deployments
kubectl get services
kubectl get pods
```

### 5. Access the Application
```bash
# Get the URL for the Flask frontend service
minikube service flask-service --url

# Open the URL in your browser to access the application
```

## 🔍 Monitoring and Troubleshooting

### View Logs
```bash
# View frontend logs
kubectl logs -l app=flask-frontend

# View backend logs
kubectl logs -l app=express-backend
```

### Check Pod Status
```bash
# Get detailed information about pods
kubectl describe pods

# Get pod status
kubectl get pods -o wide
```

## 🧹 Cleanup

To clean up and remove all resources:
```bash
# Delete all deployments and services
kubectl delete -f k8s/

# Stop Minikube
minikube stop

# Optional: Delete Minikube cluster
minikube delete
```

## 📝 Notes

- The application uses local images, so make sure to rebuild the images if you  make any changes to the code
- The frontend service is exposed using a NodePort service type
- The backend service is only accessible within the cluster
- Make sure all pods are in "Running" state before accessing the application

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚙️ Technologies Used

- Python (Flask)
- Node.js (Express)
- Docker
- Kubernetes
- Minikube

---

## 🐳 Step-by-Step Guide

### 1. Start Minikube

```bash
minikube start

2. Use Minikube Docker Environment

  eval $(minikube docker-env)

3. Build Docker Images
 
  docker build -t flask-frontend:latest ./flask-frontend
  docker build -t express-backend:latest ./express-backend

4. Deploy Kubernetes Resources

  kubectl apply -f k8s/


 5. Check Deployments & Services

  kubectl get all

6. Access Flask Frontend
 
  minikube service flask-service --url


🔁 How it Works

- Flask Frontend calls the Express Backend at /api using the backend service name.

- Communication is done inside the Kubernetes cluster using service discovery (express-service).

- You can scale pods and services easily with Kubernetes commands.

📂 Useful Commands

- kubectl delete -f k8s/                 # Clean up
- kubectl logs <pod-name>                # View logs
- minikube dashboard                     # Open Kubernetes UI
