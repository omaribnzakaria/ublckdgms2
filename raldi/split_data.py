import os

input_file = "Build/build.data"
chunk_size = 99 * 1024 * 1024  # 99MB to be safe

with open(input_file, "rb") as f:
    index = 0
    while chunk := f.read(chunk_size):
        with open(f"{input_file}.part{index:03d}", "wb") as out:
            out.write(chunk)
            print(f"Written part {index}")
        index += 1

print(f"Done! {index} parts created.")
