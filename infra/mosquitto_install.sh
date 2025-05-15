#!/bin/sh

sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable --now mosquitto.service

echo listener 1883 | sudo tee -a /etc/mosquitto/mosquitto.conf
echo allow_anonymous true | sudo tee -a /etc/mosquitto/mosquitto.conf
sudo systemctl restart mosquitto.service