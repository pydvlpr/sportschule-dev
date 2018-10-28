#!/bin/bash
#############################################################
#                                                           #
# Helper Script zum Starten des Django Servers              #
# mit frischen Datenbank-Migrationen                        #
# Vor dem Start werden Änderungen der Datenmodelle erkannt  #
# und die Datenbank aktualisiert                            #
#                                                           #
#############################################################

arg=$1
echo -e "\nDieses Script führt aus:\n"
echo -e "\t- Django Migrationen für die Datenbank"
echo -e "\t- Migrationen anwenden"
echo -e "\t- Starten des Development Servers"
echo
echo -e "Wenn aufgrund von DB-Fehlern alle\n"
echo -e "\t- __pycache__-Files\n\t- Migrationen\n"
echo -e "gelöscht werden sollen:\n\n $0 errors\n\n"

read -e -n1 -p "Verstanden und fortfahren? J/N " auswahl

if [[ $auswahl != 'J' ]]; then
    exit
fi

if [[ $1 == "errors" ]]; then

    echo -e "\nAchtung! Dieses Script löscht alle pycache-files"
    echo "und bisherigen Mirgations"
    echo
    echo "Hierdurch sollen Fehler bei der Aktualisierung der Datenbankstruktur"
    echo "vermieden werden!"
    echo

    read -e -n1 -p "Fortfahren? J/N " choice

    if [[ $choice == "J" ]] ;then

        echo "in if"

        echo -e "Lösche alle __pycache__ Dateien\n"
        rm -f kursverwaltung/__pycache__/*
        rm -f kursverwaltung/models/__pycache__/*

        echo -e "Lösche vorhandene Migrations\n"
        rm -f kursverwaltung/migrations/00*.py
    else
        echo -e "\nAuf Wiedersehen.\n"
        exit
    fi
fi

echo -e "\nÄnderungen der Datenmodelle erkennen und für DB-Migration vorbereiten"
python manage.py makemigrations

echo -e "\nMigration von Änderungen der Datenmnodelle"
python manage.py migrate

echo -e "\nServer starten..."
python manage.py runserver

echo -e "\n\nAlles gut gegangen? Wenn es fehler gab versuche:\n"
echo -e "$0 errors\n\n"
