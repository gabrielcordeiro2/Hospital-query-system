<div align="center">
  <img height="300em" src="https://user-images.githubusercontent.com/100642061/194758661-5d39710c-b7a7-4b97-8f64-fd8bebfefceb.gif">
</div>

<div align="center">
  <img height='20' src='https://img.shields.io/github/stars/gabrielcordeiro2/Hospital-query-system.svg' />
  <img height='20' src='https://img.shields.io/badge/License-MIT-red.svg' />
  <img height='20' src='https://img.shields.io/github/forks/gabrielcordeiro2/Hospital-query-system.svg' />

  [<img height='25' src='https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=blue' alt='linkedin'>](https://www.linkedin.com/in/gabrielcdev/)
  [<img height='25' src='https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=#615352' alt='instagram'>](https://www.instagram.com/krd.gabriel/)

I made a Hospital query system, which manages general tasks that occur in daily work of a front desk attendant.

  <img src="https://user-images.githubusercontent.com/100642061/194762368-dee83608-0a76-4dae-86c2-d0d0e70174e9.png" height="100px" width="720px" />
</div>

## The idea:

I wanted to challenge myself to do a different type of portfolio project, as I learned about the Backend, I was curious about how the systems that served me on a day-to-day basis worked, and from that came the idea of making a hospital system.

## Requirements to run:

**(Optional)** If you want to run this project using **Docker**, click [here](https://github.com/gabrielcordeiro2/Hospital-query-system/blob/main/UsingDocker.MD).

You will need to install all dependencies below to run:

### for Python:

1.  Python 3.8.10+
2. `git clone https://github.com/gabrielcordeiro2/Hospital-query-system`
3. `pip3 install -r requirements.txt`

### for Database:

1.  PostgreSQL
2.  postgres empty database called as `postgres` with port `5432`
3.  `.env` file created inside project, containing `DATABASE_URI=postgresql://postgres:123@localhost:5432/postgres`

## How to use

- You can found my documentation [here](https://documenter.getpostman.com/view/21448782/2s83ziMiKD).
- Run `src/api/app.py` to start API Server.
- All endpoint methods, except `/login` needs a JWT Token to use.
- If you want to populate the database, run `src/api/populate_db.py`

## Skills that I learned:

- **Database management**

  Using: PostgreSQL, SQLAlchemy (ORM), Database modeling (UML Diagram).

- **Python Backend development**
  
  Using: Docker, Flask, REST Apis, JWT Auth.

- **Rest API Documentation**
  
  Using: Postman and ThunderClient.
  
  
| UML Database diagram |
|:--:|
|![space-1.jpg](https://user-images.githubusercontent.com/100642061/194748406-81511f29-45a6-4654-af31-9c6cc565457d.png)|
I made this UML diagram using [LucidApp](https://lucid.app/documents#/dashboard).
