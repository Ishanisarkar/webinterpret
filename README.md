#### Project needs .env with db_uri parameter 
Also alembic.ini needs this url in the file if it needs to be updated.
#### Commands to run


docker-compose up

docker build -t testwebinterpret .

alembic upgrade head

docker run testwebinterpret




