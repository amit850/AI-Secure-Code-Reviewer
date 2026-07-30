import hashlib

password = "admin123"

digest = hashlib.md5(password.encode()).hexdigest()

print(digest)