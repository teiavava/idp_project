# Magazin Virtual de Telefoane

# Descriere

Proiectul propune realizarea unei arhitecturi care să expună utilizatorului o interfață web pentru interacționarea cu un magazin de telefoane.
Utilizatorul se va putea loga, își va putea crea cont, în cazul în care nu are deja unul, va putea vizualiza gridul de produse,
detalii despre acestea, precum si să le adauge în coșul de cumpărături și să le comande.

# Docker

1. run `docker-compose up --build`

# Arhitectura proiectului

1. Web Client
1. Kong Api Gateway
1. Authentication and Authorization Microservice
1. Users Database - MongoDB
1. Admin Service
1. IO Service
1. Phones Service


# Docker Swarm

git clone https://gitlab.com/teiavava/proiect_idp.git
cd proiect_idp
chmod +rwx create_images.sh deploy.sh

./create_images.sh

./deploy.sh

# To check the state of the services, please run:
docker service ls

# To check the logs of a specific service, please run:
docker service logs idp_{service_name}

docker stack deploy port... portainer
