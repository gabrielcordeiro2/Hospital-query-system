## Requirements to run in Docker:

1. Run `git clone https://github.com/gabrielcordeiro2/Hospital-query-system` in terminal.
2. Create a `.env` file inside root project, containing `DATABASE_URI=postgresql://postgres:123@postgresNet:5432/postgres`
3. Enter inside project's folder using `cd Hospital-query-system`
4. Run `docker build -t hospital_image .` in terminal.
5. Run this command to create Postgres Container:
```
docker run -d --name postgresNet --network mynetwork -v postgresVolumeNet:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres postgres
```
5. Run this command to create API Container:
```
docker run -d --name api_container --network mynetwork -p 5000:5000 -e API_HOST=0.0.0.0 -e API_PORT=5000 hospital_image
```
Docker Container names are respectively:
1. `api_container` runs the API.
2. `postgresNet` runs the Postgres Database.

- use `docker stop container_name` to stop this service.
- use `docker start container_name` to start this service.
- use `docker rm container_name` to delete this service.

## How to use

- You can found my documentation [here](https://documenter.getpostman.com/view/21448782/2s83ziMiKD).
- Run `src/api/app.py` to start API Server.
- All endpoint methods, except `/login` needs a JWT Token to use.

## Skills that i learned:

- **Database manage**

  Using: PostgreSQL, SQLAlchemy (ORM), Database modeling (UML Diagram).

- **Python Backend development**
  
  Using: Docker, Flask, REST Apis, JWT Auth.

- **Rest API Documentation**
  
  Using: Postman and ThunderClient.
  
  
| UML Database diagram |
|:--:|
|![space-1.jpg](https://user-images.githubusercontent.com/100642061/194748406-81511f29-45a6-4654-af31-9c6cc565457d.png)|
I made this UML diagram using [LucidApp](https://lucid.app/documents#/dashboard).