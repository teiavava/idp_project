docker swarm leave --force

docker swarm init --advertise-addr $(ifconfig eth0 | awk '/inet /{print $2}' | cut -f2 -d':')

docker stack deploy -c kong-stack.yml idp
docker service ls
# docker service logs idp_io-service