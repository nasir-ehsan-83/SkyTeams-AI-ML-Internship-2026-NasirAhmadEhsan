import os 

# rename specific file 
def rename_file(old_name: str, new_name: str):
    return os.rename(str(old_name), str(new_name))