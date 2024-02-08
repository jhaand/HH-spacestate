#/bin/bash

PHP_FOLDER='./php'

cd $PHP_FOLDER 
if [ -e secretsss.php ] ; then 
    DEST_FOLDER='/srv/www/hackerhotel/html/'

    chmod 664 *.php
    chmod 640 secretsss.php
    cp index.php spacestate.php throwswitch.php secretsss.php $DEST_FOLDER
    mkdir -p $DEST_FOLDER'/img/'
    cp ../share/*.png $DEST_FOLDER'/img/'
    #chown -R www-data:www-data $DEST_FOLDER
else
    echo "Run this script from the './php/' directory of the archive."
fi
cd ..

