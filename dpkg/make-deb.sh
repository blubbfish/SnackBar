#!/bin/bash

HOMEDIR=$HOME
ROOT="$HOMEDIR/deb"
SOURCE=".."

DEBIAN="$ROOT/DEBIAN"
EXEC="$ROOT/usr/local/bin/snackbar"
SYSTEMD="$ROOT/lib/systemd/system"

VMAJOR=$(grep -e "^version = " ../Snackbar/__init__.py | cut -d'"' -f 2 | cut -d'.' -f 1)
VMINOR=$(grep -e "^version = " ../Snackbar/__init__.py | cut -d'"' -f 2 | cut -d'.' -f 2)
VBUILD=$(grep -e "^version = " ../Snackbar/__init__.py | cut -d'"' -f 2 | cut -d'.' -f 3)
ARCHT=$1

mkdir -p $DEBIAN
mkdir -p $EXEC
mkdir -p $SYSTEMD

cp control $DEBIAN
sed -i s/Version:\ x\.x-x/"Version: $VMAJOR.$VMINOR-$VBUILD"/ $DEBIAN/control
sed -i s/Architecture:\ any/"Architecture: $ARCHT"/ $DEBIAN/control
chmod 755 $DEBIAN -R

cp snackbar.service $SYSTEMD
chmod 644 $SYSTEMD/snackbar.service

cp $SOURCE/defaultSettings.csv $EXEC
cp $SOURCE/README.md $EXEC
cp $SOURCE/requirements.txt $EXEC
cp $SOURCE/SnackBar.py $EXEC
cp $SOURCE/userList.csv $EXEC
find $SOURCE/Snackbar/ -type d -exec mkdir -p $EXEC/Snackbar/{} \;
find $SOURCE/Snackbar/ -type f -name \*.py -exec cp {} $EXEC/Snackbar/{} \;
find $SOURCE/Snackbar/static -type f -exec cp {} $EXEC/Snackbar/{} \;
rm $EXEC/Snackbar/static/images -rf
rm $EXEC/Snackbar/static/*.xls -f
find $SOURCE/Snackbar/templates -type f -exec cp {} $EXEC/Snackbar/{} \;
find $EXEC -type d -exec chmod 755 {} \;
find $EXEC -type f -exec chmod 644 {} \;

dpkg-deb --build $ROOT
mkdir -p ../../Builds
mv $HOMEDIR/deb.deb ../../Builds/"$ARCHT-snackbar_$VMAJOR.$VMINOR-$VBUILD.deb"
rm $HOMEDIR/deb -r