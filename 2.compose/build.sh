#!/bin/sh
docker build -t base recipes
docker build -t breakfast recipes/breakfast
docker build -t lunch recipes/lunch
docker build -t dinner -f recipes/Dockerfile.dinner recipes
docker build -t fe fe
