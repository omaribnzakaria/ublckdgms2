import os

def split_file(file_path, chunk_size_mb=99):
    chunk_size = chunk_size_mb * 1024 * 1024
    part_num = 0
    
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            part_filename = f'part_{part_num}'
            with open(part_filename, 'wb') as part_file:
                part_file.write(chunk)
            
            print(f"Created: {part_filename}")
            part_num += 1

split_file('valve.zip')
# Usage:
# split_file('my_large_video.mp4')