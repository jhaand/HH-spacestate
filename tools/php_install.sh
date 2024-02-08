#/bin/bash

if [ -e secretsss.php ] ; then 
    DEST_FOLDER='/srv/www/hackerhotel/html/'

    cp *.html *.php *.json $DEST_FOLDER
    mkdir -p $DEST_FOLDER'/img/'
    cp ../share/HH_logo_open.png ../share/HH_logo_closed.png $DEST_FOLDER'/img/'
    #chown -R www-data:www-data $DEST_FOLDER
else
    echo "Run this script from the './php/' directory of the archive."
fi
