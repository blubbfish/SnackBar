#!/bin/bash
sqlite3 -batch CoffeeDB.db "ALTER TABLE user ADD startmoney type float"
sqlite3 -batch CoffeeDB.db "CREATE TABLE \`cashdesk\` (\`cashid\` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \`price\` FLOAT NOT NULL DEFAULT 0.0, \`date\` DATETIME NOT NULL, \`item\` TEXT NOT NULL);"
mv CoffeeDB.db SnackBar/