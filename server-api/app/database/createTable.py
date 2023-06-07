from database import dbCreate

dbCreate("CREATE TABLE IF NOT EXISTS user (user TEXT, password TEXT, email TEXT)")
dbCreate("CREATE TABLE IF NOT EXISTS invite (userOne TEXT, userTwo TEXT, pubkey TEXT)")
