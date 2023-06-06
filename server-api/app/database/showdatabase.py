from database import dbGet
rows = dbGet("SELECT * FROM user")
print("User")
print(rows)
rows = dbGet("SELECT * FROM invite")
print("Invite")
print(rows)

