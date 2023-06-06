from database import dbGet

dbGet("CREATE TABLE IF NOT EXISTS user (user TEXT, password TEXT, email TEXT)")
dbGet("CREATE TABLE IF NOT EXISTS invite (userOne TEXT, userTwo TEXT, pubkey TEXT)")
