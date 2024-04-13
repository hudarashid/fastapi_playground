docker-compose build = to build the docker image
docker-compose up = run the docker images

alembic init alembic = create migration folder

docker-compose run app alembic revision --autogenerate -m "New Migration" = makemigration file
docker-compose run app alembic upgrade head = migrate (create) the file in the db
