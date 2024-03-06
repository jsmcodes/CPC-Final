import os
import subprocess

def convert_qrc_to_python(qrc_file_path, output_python_path):
    command = f"pyrcc5 {qrc_file_path} -o {output_python_path}"
    subprocess.run(command, shell=True)

def convert_all_qrc_files(resource_folder):
    qrc_files = [file for file in os.listdir(resource_folder) if file.endswith(".qrc")]

    for qrc_file in qrc_files:
        qrc_file_path = os.path.join(resource_folder, qrc_file)
        output_python_path = f"{os.path.splitext(qrc_file)[0]}_rc.py"
        convert_qrc_to_python(qrc_file_path, output_python_path)

if __name__ == "__main__":
    resource_folder = "Resource"
    convert_all_qrc_files(resource_folder)
