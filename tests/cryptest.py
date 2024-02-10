import bcrypt


password = b"SecretPasswodr55"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("hashed: ", hashed)

if bcrypt.checkpw(password, hashed):
    print('It matches!')
else:
    print('Didn\'t match')