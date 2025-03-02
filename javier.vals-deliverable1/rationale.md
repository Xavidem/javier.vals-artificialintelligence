Rationale for Text Extraction and Analysis
Author: Javier Vals Lopez
Reason for the project: Delivery of deliverable 1 for the subject of Artificial Intelligence And Open Science In Research Software Engineering

# 1. Introduction

This document provides a detailed explanation of how the data extraction, processing, process failures and visualization were validated in this project.

# 2. Data Extraction Validation

Tool Used: Grobid, provided by the teachers (https://github.com/kermitt2/grobid)

Grobid was used to extract structured information from 10 open-access papers in PDF format, which have been taken from the open website ArXiv.org.

The XML outputs were inspected to ensure that key elements such as the abstract, figures, and references were correctly parsed.

Validation: The extracted XML files were manually checked to ensure the presence of &lt;abstract&gt;, &lt;figure&gt;, and &lt;ref&gt; elements.

# 3. Abstract Extraction Validation

Script Used: extract_data.py

First, I initially had issues extracting abstracts due to varying XML structures. I was downloading the XML files with the Full Header option and not Full Text.

The correct XPath expressions were determined by inspecting the XML output and adjusting the script to handle abstracts inside &lt;s&gt; and &lt;p&gt; elements.

Validation: I printed the full &lt;abstract&gt; content before processing it with another Python script (extract_abstract_data.py), confirming that the correct text was extracted.

The final output was stored in results.json.

# 4. Figures Count Validation

Script Used: extract_data.py

The count of figures was extracted from &lt;figure&gt; tags (although I have also left the &lt;graphic&gt; option in case other papers include it as well).

Validation: Manually checked the XML files for the presence of &lt;figure&gt; tags.

The counts in results.json were compared with the number of figures present in the PDF files.

# 5. Keyword Cloud Validation

Script Used: keyword_cloud.py

The script generates a word cloud based on the words in the extracted abstracts.

Stopwords were considered but not removed.

Validation: The generated word cloud was visually inspected to ensure the main topics of the papers were reflected in the visualization.

# 6. Figures Count Visualization Validation

Script Used: figures_plot.py

The script generates a bar chart of the number of figures per article.

Validation: The counts from results.json were manually checked (in one of the papers) against the bar chart.

# 7. Links Extraction Validation

Script Used: extract_data.py

Extracted from &lt;ref&gt; tags in the XML files.

Validation: Manually checked (in one of the papers) against the reference section of the PDFs.

# 8. Computational Environment

The required Python libraries are listed in requirements.txt.

The entire experiment is containerized using Docker for reproducibility.

# 9. Reproducibility

All scripts and dependencies are included in this repository.

The Dockerized setup allows the experiment to be easily executed in any environment supporting Docker.

Instructions for running the experiment are provided in README.md.

# 10. Conclusion

Each extraction and visualization step has been carefully validated to ensure accuracy and reproducibility. The project provides a complete pipeline for extracting and analyzing text from research papers using Grobid.

