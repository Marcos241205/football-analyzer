#!/bin/bash

# Nombre de la imagen
IMAGE_NAME=football-analyzer

# Construir la imagen
echo "🔨 Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Ejecutar el contenedor
echo "🚀 Ejecutando el contenedor..."
docker run -it $IMAGE_NAME
