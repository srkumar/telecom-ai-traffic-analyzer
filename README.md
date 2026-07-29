# Telecom AI Traffic Analyzer

## Overview

Telecom AI Traffic Analyzer is a Python-based application designed to analyze A2P messaging traffic logs and generate operational insights. The application processes telecom traffic using Python and Pandas to calculate key performance indicators (KPIs), perform country-wise and operator-wise analysis, and generate structured reports. An optional AI layer can be used to produce executive summaries and business-ready operational reports.

This project demonstrates how traditional data analytics and Generative AI can work together in telecom operations.

---

## Features

* Overall KPI Analysis
* Country-wise Traffic Analysis
* Operator-wise Traffic Analysis
* Daily Traffic Report Generation
* Top Countries by Traffic
* Top Operators by Traffic
* Delivery & Failure Percentage Calculation
* AI-ready Prompt Builder
* AI-assisted Executive Summary (Gemini API)
* Modular Python Project Structure

---

## Technologies Used

* Python 3.x
* Pandas
* Google Gemini API
* Prompt Engineering
* Git & GitHub

---

## Project Structure

```text
telecom-ai-traffic-analyzer/
│
├── app.py
├── kpi.py
├── country_analysis.py
├── operator_analysis.py
├── report_builder.py
├── prompt_builder.py
├── ai_engine.py
├── logs.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Architecture

```text
Telecom Logs (CSV)
        │
        ▼
Data Processing (Pandas)
        │
        ├── KPI Analysis
        ├── Country Analysis
        ├── Operator Analysis
        │
        ▼
Structured Report
        │
        ▼
Prompt Builder
        │
        ▼
Gemini AI (Optional)
        │
        ▼
Executive Summary
RCA
Business Impact
Recommendations
```

---

## Sample Output

The application generates reports including:

* Overall Traffic
* Delivered Messages
* Failed Messages
* Delivery Percentage
* Country Summary
* Top Countries by Traffic
* Operator Summary
* Top Operators by Traffic
* Date-wise Country Report
* Date-wise Operator Report

---

## Installation

Clone the repository:

```bash
git clone https://github.com/srkumar/telecom-ai-traffic-analyzer.git
```

Move to the project directory:

```bash
cd telecom-ai-traffic-analyzer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

---

## Future Enhancements

* Streamlit Dashboard
* Interactive Charts
* Trend Analysis
* Hourly Traffic Analysis
* Error Code Analysis
* Sender Analysis
* Account Analysis
* PDF Report Generation
* Automated Daily Report Scheduling

---

## Objectives

This project demonstrates practical implementation of:

* Python Programming
* Pandas Data Analysis
* Telecom KPI Reporting
* Modular Software Design
* Prompt Engineering
* Generative AI Integration
* Git & GitHub Version Control

---

## Author

**Shashi Ranjan Kumar**

Telecom Operations | A2P Messaging | Python | Pandas | Generative AI | Technical Operations

GitHub: https://github.com/srkumar
