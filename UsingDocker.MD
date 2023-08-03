## Requirements to run in Docker:

### Resources:
If you don't have  docker, install using [this](https://docs.docker.com/get-docker/) guide.

### How to run:
1. Run `git clone https://github.com/gabrielcordeiro2/Hospital-query-system` in terminal.
2. Enter inside project's folder using `cd Hospital-query-system`
3. Create a `.env` file in root project, containing: `DATABASE_URI=postgresql://postgres:123@postgresNet:5432/postgres` and `API_HOST=0.0.0.0`
4. Run `docker build -t hospital_image .` in terminal.
5. Run this command to execute both api_container and PostgresNet:
```
docker compose up
```

6. Run this command below to populate database with sample data:
```
docker exec -it api_container python ./src/api/populate_db.py
```

Docker Container names are respectively:
1. `api_container` runs the API.
2. `postgresNet` runs the Postgres Database.

- use `docker exec -it api_container bash` to enter inside api container.
- use `docker compose up` to start this service.
- use `docker compose down` to delete this service.
- use `docker compose restart` to restart this service.

If you want to expose PostgresNet to localhost, please uncomment ports section in `docker-compose.yaml`

## How to use

- You can found my documentation [here](https://documenter.getpostman.com/view/21448782/2s83ziMiKD).
- Run `src/api/app.py` to start API Server.
- All endpoint methods, except `/login` needs a JWT Token to use.

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