cd ApiGatewayMicroservice/
docker build -t api-gateway .
cd ../Authentication
docker build -t authentication .
cd ../Admin
docker build -t admin .
cd ../IO
docker build -t io .
cd ../Phones
docker build -t phones .