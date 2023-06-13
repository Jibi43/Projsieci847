import os

def count_files(path, extensions):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                count += 1
    return count

def generate_report(count, extensions, output_format, output_directory):
    if output_format == 'txt':
        output_path = os.path.join(output_directory, 'report.txt')
        with open(output_path, 'w') as f:
            f.write(f"Total files: {count}")
            f.write('\n')
            f.write("File count per extension:")
            file_counts = {ext: 0 for ext in extensions}
            for root, dirs, files in os.walk(path):
                for file in files:
                    for ext in extensions:
                        if file.endswith(ext):
                            file_counts[ext] += 1
            for extension, files_count in file_counts.items():
                f.write('\n')
                f.write(f"{extension}: {files_count}")
    elif output_format == 'html':
        output_path = os.path.join(output_directory, 'report.html')
        with open(output_path, 'w') as f:
            f.write('<html><body>')
            f.write(f"<h1>Total files: {count}</h1>")
            f.write("<h2>File count per extension:</h2>")
            f.write('<ul>')
            file_counts = {ext: 0 for ext in extensions}
            for root, dirs, files in os.walk(path):
                for file in files:
                    for ext in extensions:
                        if file.endswith(ext):
                            file_counts[ext] += 1
            for extension, files_count in file_counts.items():
                f.write(f"<li>{extension}: {files_count}</li>")
            f.write('</ul>')
            f.write('</body></html>')

path = input("Enter the directory path: ")
extensions = input("Enter the file extensions (separated by spaces): ").split()
output_format = input("Enter the output format (txt or html): ")
output_directory = input("Enter the output directory: ")

count = count_files(path, extensions)
generate_report(count, extensions, output_format, output_directory)
print("Report generated successfully.")
