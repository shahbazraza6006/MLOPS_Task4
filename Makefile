.PHONY: all build run

all: build run

build:
    docker build -t car-price-predictor .

run:
    docker run -p 5000:5000 car-price-predictor
