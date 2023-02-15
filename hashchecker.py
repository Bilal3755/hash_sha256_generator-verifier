import hashlib

def gen_hash_sha2(user_file_path):
    # rb below opens and reads file in binary along with open fn
    with open(user_file_path, 'rb') as f:
        # Create a new SHA-256 hash object
        sha256 = hashlib.sha256()
        # Update the hash object with the file contents
        sha256.update(f.read())
        return sha256.hexdigest()

user_file_path = input("Enter the file path: ")

# hash_generation_of_user_file
file_hash = gen_hash_sha2(user_file_path)
print("SHA-256 hash:", file_hash)

# For hash comparison
user_hash = input("Enter the  SHA-256 hash for verification: ")

# Compare the expected hash with the actual hash
if user_hash == file_hash:
    print("Hashes match, file is authentic!")
else:
    print("Hashes match failed.")
