import zipfile

with zipfile.ZipFile("my-zip.zip", mode="r") as archive:
    archive.extract("wmt1.csv", path="output_dir/")
    archive.extract("wmt2.csv", path="output_dir/")