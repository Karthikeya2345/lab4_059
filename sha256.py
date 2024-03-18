import hashlib
file=""#file location

BLOCK_SIZE=65536
file_hash=hashlib.sha256()
with open(file,'rb') as f:
    