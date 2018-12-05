#!/bin/bash
sqlite3 CoffeeDB.db -cmd "ALTER TABLE user ADD startmoney type float" -batch
sqlite3 CoffeeDB.db -cmd "CREATE TABLE `cashdesk` (`cashid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	`price`	FLOAT NOT NULL DEFAULT 0.0,	`date`	DATETIME NOT NULL,	`item`	TEXT NOT NULL);" -batch
mv CoffeeDB.db SnackBar/