#!/bin/bash
#############################################################
#                                                           #
# Helper Script zum Starten des Django Servers              #
# Vor dem Start werden Änderungen der Datenmodelle erkannt  #
# und die Datenbank aktualisiert                            #
#                                                           #
#                                                           #
#############################################################

echo "Änderungen der Datenmodelle erkennen und für DB-Migration vorbereiten"
python manage.py makemigrations

echo "Migration von Änderungen der Datenmnodelle"
python manage.py migrate

echo "Server starten..."
python manage.py runserver

