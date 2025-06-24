import os
import zipfile
import gdown

# Your file IDs (replace with real ones)
drive_files = {
    "train": "1nklErujyjjZrD9VYlmqKCd3m9m88B1F_",      #https://drive.google.com/file/d/1nklErujyjjZrD9VYlmqKCd3m9m88B1F_/view?usp=drive_link
    "val": "13D5sSj1e3JP63bVN7wXRK0S_CZcN9-97",     #https://drive.google.com/file/d/13D5sSj1e3JP63bVN7wXRK0S_CZcN9-97/view?usp=drive_link
    "test": "1F_tnBTlJS4qwmt_UZd9Ou6LPLZ0-fn08"        #https://drive.google.com/file/d/1F_tnBTlJS4qwmt_UZd9Ou6LPLZ0-fn08/view?usp=drive_link
}

os.makedirs("data", exist_ok=True)

for name, file_id in drive_files.items():
    zip_path = f"{name}.zip"
    output_folder = os.path.join("data", name)
    os.makedirs(output_folder, exist_ok=True)

    # Download
    print(f"Downloading {name}.zip from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", zip_path, quiet=False)

    # Extract
    print(f"Extracting to data/{name}/")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    os.remove(zip_path)
    print(f"{name}.zip extracted and cleaned up.\n")
