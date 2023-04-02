import zipfile

filenames = ["wmt1.csv", "wmt2.csv"]

with zipfile.ZipFile("my-zip.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename)