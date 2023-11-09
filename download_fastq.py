import subprocess
import csv
import os

# Function to read SRR IDs and study names from a CSV file and create a dictionary
def read_csv_config(config_file):
    srr_to_study = {}
    with open(config_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            srr_to_study[row['SRR_ID']] = row['Study']
    return srr_to_study

# Function to download and convert SRR accession to FASTQ format
def download_fastq(srr_id, study_name, output_base_dir='downloaded_data'):
    try:
        # Create a directory for the study if it doesn't exist
        study_dir = os.path.join(output_base_dir, study_name)
        os.makedirs(study_dir, exist_ok=True)

        # Use prefetch to download data
        subprocess.run(['prefetch', srr_id, '-o', study_dir], check=True)

        # Use fastq-dump to convert to FASTQ format
        subprocess.run(['fastq-dump', '--split-files', srr_id, '--outdir', study_dir], check=True)

        print(f'Successfully downloaded and converted {srr_id} from {study_name} to FASTQ format.')
    except subprocess.CalledProcessError as e:
        print(f'Error downloading or converting {srr_id}: {e}')