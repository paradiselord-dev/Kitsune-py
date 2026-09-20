Kitsune: Python 3.11 & NumPy 2.x Modernized Fork
An open-source, unsupervised online Network Intrusion Detection System (NIDS) based on an Ensemble of Autoencoders (KitNET) and incremental feature extraction (AfterImage).

This fork has been refactored, updated, and optimized for modern Python environments (Python 3.11+) and high-performance numerical computing libraries (NumPy 2.x).

- Key Improvements in this Fork
NumPy 2.x Compliance: Migrated legacy and deprecated numerical aliases (such as np.Inf / np.nan) to modern standards, ensuring seamless execution without compatibility warnings or runtime failures.

Modern Python Support: Fully validated and tested on Python 3.11 with clean virtual environment isolation (.venv).

Reproducible Setup: Locked dependency chain via requirements.txt.

Robust Anomaly Detection: Verified against real-world benchmark traffic captures (e.g., Mirai botnet pcap), maintaining high-precision RMSE reconstruction peaks during anomalous events.

- Installation & Setup
Clone the repository:

Bash
git clone https://github.com/paradiselord-dev/Kitsune-py.git
cd Kitsune-py
Create and activate a virtual environment:

On Windows (PowerShell):

PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
On Linux / macOS:

Bash
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

Bash
pip install --upgrade pip
pip install -r requirements.txt
📊 Architecture Overview
Kitsune operates in two primary stages without requiring prior labeling of network packets:

AfterImage (Feature Extraction): Extracts statistical summaries of network traffic streams in real-time using exponential decaying moving averages across various time windows.

KitNET (Anomaly Detector): An ensemble of lightweight autoencoders structured in layers:

Layer 1 (Mapping Layer): Evaluates individual feature correlations.

Layer 2 (Reduction Layer): Compresses the outputs of Layer 1.

Output Layer: A final autoencoder that computes the aggregate Root Mean Square Error (RMSE). Sudden spikes in RMSE indicate network anomalies or intrusion attempts.

- Quickstart Example
Run the primary script against a target packet capture (.pcap) file to inspect anomaly scores:

Python
from Kitsune import Kitsune

# Configuration parameters
packet_path = "mirai.pcap" # Path to target pcap file
maxAE = 10                  # Maximum size for any autoencoder in the ensemble
FMgrace = 5000              # Number of instances for feature mapping grace period
ADgrace = 50000             # Number of instances for anomaly detector grace period

# Initialize Kitsune engine
Kitsune_instance = Kitsune(packet_path, maxAE, FMgrace, ADgrace)

# Execute processing pipeline
# rmse_results = Kitsune_instance.procall()

- References & Credits
Original Paper: Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection (Yisroel Mirsky, Tomer Doitshman, Yuval Elovici, Asaf Shabtai — NDSS).

Fork maintained by paradiselord-dev.