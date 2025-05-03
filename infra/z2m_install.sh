#!/bin/sh

USER=zigbee2mqtt
GROUP=dialout
INSTALL_DIR=/opt/zigbee2mqtt

sudo apt-get install -y curl
sudo curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs git make g++ gcc libsystemd-dev
npm install -g pnpm

id -u ${USER} || sudo useradd -rmN ${USER}
sudo gpasswd -a ${USER} ${GROUP}

sudo mkdir "${INSTALL_DIR}"
sudo git clone --depth 1 https://github.com/Koenkk/zigbee2mqtt.git "${INSTALL_DIR}"
sudo chown -R ${USER}:${GROUP} "${INSTALL_DIR}"

sudo -D "${INSTALL_DIR}" -u ${USER} pnpm install --frozen-lockfile
sudo -D "${INSTALL_DIR}" -u ${USER} pnpm start
