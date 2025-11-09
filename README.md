# Text Summarizer using Hugging Face Transformers  

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange) ![AWS](https://img.shields.io/badge/AWS-Deployment-yellow) ![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-green)  

---

## **Project Overview**

This project implements a **Text Summarization system** using state-of-the-art **Hugging Face Transformers**. It takes long text input and produces concise summaries while maintaining the core meaning.  

The project emphasizes:  
- **Modular coding** for better maintainability.  
- **DVC (Data Version Control)** for managing datasets and models.    
- **CI/CD deployment** on AWS using **GitHub Actions**.  

---

## **Features**

- Summarizes articles, news, or documents automatically.  
- Easy to extend to different Transformer models.  
- Supports GPU acceleration for faster inference.  
- Continuous integration and deployment using GitHub Actions.  
- Containerisation using Docker.    

---

## **Project Structure**
text_summarizer/
├── main.yaml
├── .gitignore
├── .venv
├── artifacts
│   └── artifacts_root
├── config
│   └── config.yaml
├── Dockerfile
├── LICENSE
├── logs
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── research
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   ├── 05_model_evaluation.ipynb
│   ├── Text_Summarization.ipynb
│   └── trials.ipynb
├── samsum_dataset.zip
├── setup.py
├── src
│   └── TextSummarizer
│       ├── __init__.py
│       ├── __pycache__
│       ├── components
│       ├── config
│       ├── constants
│       ├── entity
│       ├── logging
│       ├── pipeline
│       └── utils
├── template.py
└── templates
    └── index.html
├─ app.py    
├─ params.yaml
├─ setup.py
├─ template.py   
├─ requirements.txt
└─ README.md

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml
9. app.py

# INSTALLATION
### STEPS:

Clone the repository

```bash
https://github.com/G-Sahil123/Text_Summarizer.git
cd Text_Summarizer
```
### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv myvenv
# Windows
myvenv\Scripts\activate
# Linux/macOS
source myvenv/bin/activate
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## Usage
### Run the full pipeline
```bash
python main.py
```
This will execute all stages sequentially
1. Data ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Evaluation