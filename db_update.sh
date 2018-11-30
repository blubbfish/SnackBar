#!/bin/bash
sqlite3 CoffeeDB.db -cmd "ALTER TABLE user ADD startmoney type float" -batch
mv CoffeeDB.db SnackBar/