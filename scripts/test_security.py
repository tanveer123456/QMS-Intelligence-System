from app.core.security import hash_password, verify_password

password = "Password123"

hashed_password = hash_password(password)

print("=" * 60)
print("Original Password :", password)
print("Hashed Password   :", hashed_password)
print("=" * 60)

is_valid = verify_password(
    password,
    hashed_password,
)

print("Password Verified :", is_valid)