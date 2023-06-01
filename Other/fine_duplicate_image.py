import hashlib

os.chdir(train_image_path)
image_filename_list = os.listdir('.')
print('[INFO] TOTAL NUMBER OF FILE : ', len(image_filename_list))

duplicates=dict()
hash_keys=dict()

FIND SET OF DUPLICATES IMAGE
for filename in tqdm(image_filename_list):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=filename
        else:
            if filehash not in duplicates:
                duplicates[filehash] = [hash_keys[filehash]]
            duplicates[filehash] += [filename]

print(duplicates)