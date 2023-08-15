# Translational Informatics Services coding interview

## General Instructions
1) Please answer all written questions in the readme file 'Answers' within each Section directory.
2) Please place all files generated into 'Answers' directory within each Section directory.

---

## Folder structure

```
.
├── README.md
├── Section_1
│   ├── ANSWERS
│   │   ├── ANSWER.md
│   │   ├── genotype_merged.txt
│   │   ├── rs1421085_plot.png
│   │   ├── rs7074440_plot.png
│   │   ├── rs9273367_plot.png
│   │   ├── rs9275530_plot.png
│   │   ├── rs9368219_plot.png
│   │   └── section1.csv
│   ├── README.md
│   ├── __init__.py
│   ├── genotypes.txt
│   ├── phenotypes.txt
│   ├── section1_solver.py
│   └── service1_workbook.ipynb
├── Section_2
│   ├── ANSWERS
│   │   ├── ANSWER.md
│   │   ├── qnorm.txt
│   │   └── violin_plot.png
│   ├── ANSWERS.md
│   ├── README.md
│   ├── TIS_raw_input1.txt
│   ├── TIS_raw_input2_regulation_status.txt
│   └── workflow_runner.py
├── Section_3
│   ├── ANSWERS
│   │   ├── ANSWERS.md
│   │   └── df.csv
│   ├── README.md
│   ├── section3_workbook.ipynb
│   └── section_3_assignment.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── female_data_analysis_test.py
    ├── genotype_formation_test.py
    └── male_data_analysis_test.py
```

---

## What you need before running?

- Python
- Pytest (optional - for testing)

---

## Installation

```
pip3 install -r requirements.txt
```

## How to run?


Section 1:

```
cd Section\ 1
python3 section1_solver.py
```


Section 2:

```
cd Section\ 2
python3 workflow_runner.py
```


Section 3:

```
cd Section\ 3
python3 section_3_assignment.py
```

---


Testing (optional)


```
pytest .
```
