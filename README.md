# Automated FASTQ Download and Organization

This project automates the download of FASTQ files from the Sequence Read Archive (SRA) based on SRR IDs provided in a CSV configuration file. The downloaded data is organized into study-specific directories for easy access and management.

## Prerequisites

Before running the code, ensure that you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/)
- [SRA Toolkit](https://www.ncbi.nlm.nih.gov/sra/docs/toolkitsoft/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/SRR-download.git
   
2. Navigate to the project directory:

    ```bash
    cd SRR-download

3. Install any necessary Python packages if not already installed:

    ```bash
   pip install -r requirements.txt

4. Prepare your CSV configuration file (config.csv) with the following format:

    ```bash
    SRR_ID,Study
    SRR1234567,Study1
    SRR7654321,Study2
    SRR9876543,Study1

Replace SRR_ID with the SRR accessions you want to download and Study with the corresponding study names.

5. Run the Jupyter Notebook to execute the code:

    ```bash
   jupyter notebook main.ipynb

This will initiate the download process based on the configurations provided in config.csv.

## Configuration
The functions.py file contains functions for reading the CSV configuration and downloading data.
The main.ipynb Jupyter Notebook imports functions from functions.py and executes the download process.

## Output
The downloaded FASTQ files are organized into study-specific directories under the downloaded_data directory.

## Troubleshooting
If you encounter any issues or errors during the download process, refer to the error messages and the debugging section in the code for troubleshooting.


## Author
Bhanwar Lal Puniya, Ph.D.

## License
This project is licensed under the MIT License - see the LICENSE file for details.