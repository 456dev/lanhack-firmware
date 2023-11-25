#!/bin/bash
docker run --rm -v .:/config -v /var/run/dbus:/var/run/dbus -v /var/run/avahi-daemon/socket:/var/run/avahi-daemon/socket -it --publish 6052:6052 ghcr.io/esphome/esphome
