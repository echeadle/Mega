import zipfile as zip

def extract_archive(archivepath, dest_dir):
    with zip.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("/home/echeadle/Programing/U_Python/Mega/17_day/file_compress/compressed.zip",
                    "/home/echeadle/Programing/U_Python/Mega/17_day/file_compress/dest")
