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

if [ $1 == "errors" ]; then

    echo -e "\nAchtung! Dieses Script löscht alle pycache-files"
    echo "und bisherigen Mirgations"
    echo
    echo "Hierdurch sollen Fehler bei der Aktualisierung der Datenbankstruktur"
    echo "vermieden werden!"
    echo

    read -e -n1 -p "Fortfahren? J/N " choice
    
    if [ $choice == "J" ] ;then

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

echo -e "\n\nAlles gut gegangen? Wenn es fehler gab versuche:"
echo "$0 errors"
