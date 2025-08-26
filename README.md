# Leverging LLMs for Labelling Wind Turbine Maintenance Logs with A Comparative Benchmark of Models Used

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16948633.svg)](https://doi.org/10.5281/zenodo.16948633) [![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mvmalyi/) [![ORCID](https://img.shields.io/badge/ORCID-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-1503-9798) [![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Max-Malyi) [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=FgcRBeUAAAAJ)

An open-source, reproducible framework for benchmarking Large Language Models (LLMs) for the classification of unstructured wind turbine maintenance logs. This project evaluates proprietary and open-source models on performance, cost, and calibration to support data-driven O&M in the wind energy sector.

This repository contains the full source code and supplementary materials for the paper:
> Malyi, M., Shek, J. and McDonald, A., 2025. *A Comparative Benchmark of Large Language Models for Data Labelling Applied to Wind Turbine Maintenance Logs*

---

## About The Project

The unstructured, free-text nature of wind turbine maintenance logs presents a significant barrier to automated reliability analysis. This project introduces a robust and reproducible framework to systematically evaluate the practical viability of modern LLMs for this classification task.

The framework is designed to be:
* **Reproducible:** Key parameters, model definitions, and prompts are externalised in configuration files.
* **Modular:** The code is structured with distinct classes for different model APIs, making it easy to extend.
* **Comprehensive:** The analysis goes beyond simple accuracy to include critical industrial metrics like cost, throughput, and model calibration.

---

## Repository Structure

The repository is organised to separate configuration, source code, data, and results.

```
.
# -----------------------------------------------------------------------------
# ├── Project Documentation & Setup
# -----------------------------------------------------------------------------
├── README.md                 # Main project documentation and user guide
├── technical_report.md       # Detailed report of the analysis and findings
├── used_taxonomy.md          # Description of the labelling schema used in the study
├── LICENSE                   # The open-source license for the project (MIT)
└── requirements.txt          # Python package dependencies for installation

# -----------------------------------------------------------------------------
# ├── Configurations
# -----------------------------------------------------------------------------
├── configurations/
│   └── config.yaml           # Central config for model parameters, API keys, and paths
└── prompts.json              # Dynamic prompt templates and label schemas

# -----------------------------------------------------------------------------
# ├── Source Code Modules
# -----------------------------------------------------------------------------
├── llm_clients/              # Python modules for interacting with different LLM providers
│   ├── base_client.py        # Abstract base class for all LLM clients
│   ├── google_client.py      # Client for Google's Gemini models
│   ├── ollama_client.py      # Client for locally-hosted Ollama models
│   └── openai_client.py      # Client for OpenAI's GPT models
└── utils/                    # Utility and helper scripts
    ├── config_loader.py      # Helper to load parameters from config.yaml
    ├── data_schemas.py       # Pydantic schemas to validate the structure of LLM outputs
    └── logging_config.py     # Configuration for application logging

# -----------------------------------------------------------------------------
# ├── Data & Analysis Workflow
# -----------------------------------------------------------------------------
├── input_dataset.csv  # A small dummy sample input data for running the benchmark with some columns classified 
│
├── informative_dataset_engineering/          # Notebooks for initial data preparation and engineering
│   ├── engineering_informative_dataset.ipynb # The main data preparation pipeline
│   └── translations_merge_(optional).ipynb   # Optional merge of translated descriptors
│
├── 1_run_benchmark.ipynb     # Main notebook (1): Executes the LLM benchmark
└── 2_analyse_results.ipynb   # Main notebook (2): Processes results and generates figures

# -----------------------------------------------------------------------------
# ├── Outputs (Examples of generated files)
# -----------------------------------------------------------------------------
└── outputs/                  # Default directory for all generated files
    ├── analysis_results/     # Holds figures and tables from the analysis notebook
    ├── cost_tracking/        # Logs for tracking API token usage and costs
    ├── performance_log.csv   # High-level summary log of model performance
    ├── runs/                 # Contains raw results from each timestamped benchmark run
    └── technical_report_figures/ # Contains figures used in the technical report
```

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.13.5 was used in the project
* An environment manager like `venv` or `conda` is recommended
* Required libraries installed from the `requirements.txt`

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/wind-farm-maintenance-logs-labelling-with-llms.git
    cd wind-farm-maintenance-logs-labelling-with-llms
    ```
2.  **Create and activate a virtual environment** (recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Configure API Keys:**
    Save API keys as environmental variables or open the `config.yaml` file and add your API keys for the models you wish to test. If you are using Ollama, make sure to pre-install the models queried.

---

## Usage

The workflow is divided into two main stages, executed via the Jupyter notebooks in the `/notebooks` directory.

1.  **Configure the Benchmark:**
    Before running, review the `config.yaml` file to select which models you want to run.

2.  **Run the Benchmark:**
    Execute the cells in `1_run_benchmark.ipynb`. This will iterate through your selected models, process the `input_dataset.csv`, and save the raw classification results to a timestamped directory inside `outputs/runs`.

3.  **Analyse the Results:**
    Once the benchmark is complete, configure the results path and run the cells in `2_analyse_results.ipynb`. This notebook will load the latest results, perform the analysis (calculating F1-scores, calibration, etc.), and generate the figures like the ones presented in the paper.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

Max Malyi - Max.Malyi@ed.ac.uk

Project Link: [Wind Farm Maintenance Logs Labelling with LLMs](https://github.com/your-username/wind-farm-maintenance-logs-labelling-with-llms)
