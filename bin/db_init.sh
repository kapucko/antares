#!/usr/bin/env bash

sudo -u postgres psql -c "DROP DATABASE IF EXISTS antares_core" 2>&1 > /dev/null
sudo -u postgres psql -c "DROP ROLE IF EXISTS antares" 2>&1 > /dev/null
sudo -u postgres psql -c "CREATE USER antares WITH PASSWORD 'password';" 2>&1 > /dev/null
sudo -u postgres psql -c "CREATE DATABASE antares_core WITH ENCODING 'UTF8' OWNER antares;" 2>&1 > /dev/null