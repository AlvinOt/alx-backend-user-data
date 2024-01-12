import bcrypt

# Hashing a password for storage
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return salt, hashed_password

# Checking the validity of an input password
def check_password(input_password, stored_salt, stored_hashed_password):
    hashed_password = bcrypt.hashpw(input_password.encode('utf-8'), stored_salt)
    return hashed_password == stored_hashed_password

# Example usage
if __name__ == "__main__":
    user_password = "user123"

    # Hash the password and get salt
    salt, hashed_password = hash_password(user_password)

    # Check if a login password is valid
    login_password = "user123"
    if check_password(login_password, salt, hashed_password):
        print("Password is valid!")
    else:
        print("Password is invalid!")
