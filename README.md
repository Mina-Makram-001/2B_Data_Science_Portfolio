# 2B Data Science Internship Portfolio

Welcome to my central portfolio repository for the **2B Data Science Internship**. This repository serves as an index and architectural overview of the various analytical, machine learning, and natural language processing tasks I completed during my internship. Each major task has been modularized into its own dedicated repository, linked below.

## 🌟 Internship Overview & Key Learnings

During this internship, I transitioned from foundational data analytics to building robust, end-to-end data science pipelines. Working with real-world scenarios allowed me to deepen my expertise across business intelligence, machine learning, and generative AI integrations. 

**Key Skills & Methodologies Gained:**
*   **Advanced Python Development:** Wrote modular, clean Python code for data processing, statistical modeling, and machine learning using libraries like Pandas, Scikit-Learn, and NumPy.
*   **Generative AI & NLP Integration:** Explored the cutting-edge of AI by integrating Large Language Models (LLMs) via APIs (including Gemini), evaluating prompts, and implementing Retrieval-Augmented Generation (RAG) architectures.
*   **End-to-End BI Workflows:** Bridged the gap between Python data preparation and interactive Power BI dashboarding to deliver actionable business intelligence.
*   **Version Control & Architecture:** Structured a complex, multi-repository GitHub portfolio, mastering Git workflows and environment management.

---

## 📂 Projects Overview

Below is a breakdown of the four primary tasks completed during the internship, along with their core objectives and top insights. Click on any repository name to view the source code and complete project documentation.

### 1. Countries Clustering (Machine Learning, LLM & RAG) ⭐⭐⭐
**Repository:** [Py_Countries_Clustering_ML_LLM_RAG](https://github.com/Mina-Makram-001/Py_Countries_Clustering_ML_LLM_RAG)

*   **Overview:** This project combined unsupervised machine learning with generative AI. I applied clustering algorithms to group countries based on socio-economic indicators. To enrich the analysis, I implemented a Retrieval-Augmented Generation (RAG) pipeline using an LLM to generate contextual, text-based insights explaining the defining characteristics of each cluster.
*   **Top Insights:**
    *   **Enhanced Interpretability:** While standard K-Means clustering provided the mathematical boundaries, integrating the RAG pipeline allowed the model to autonomously generate plain-English economic profiles for each cluster.
    *   **Feature Importance:** GDP per capita and life expectancy were the strongest deterministic variables in separating developed economies from developing nations in the vector space.

### 2. Sleep & Productivity Classification ⭐⭐
**Repository:** [Py_Sleep_Productivity_3Classification_MLs](https://github.com/Mina-Makram-001/Py_Sleep_Productivity_3Classification_MLs)

*   **Overview:** A supervised machine learning project aimed at predicting an individual's productivity level based on their sleep metrics and daily habits. I built and evaluated a multi-class classification model (handling 3 distinct target classes) to identify which sleep factors most heavily influence waking performance.
*   **Top Insights:**
    *   **Quality over Quantity:** The deep sleep phase and overall sleep *quality* scores were far stronger predictors of high productivity than total hours slept.
    *   **Model Performance:** Ensemble classification methods effectively handled the non-linear boundaries between the three productivity classes, outperforming baseline logistic models.

### 3. Super Store Sales Analysis (Python & Power BI) ⭐
**Repository:** [PowerBI_Py_Super_Store_Sales_Analysis](https://github.com/Mina-Makram-001/PowerBI_Py_Super_Store_Sales_Analysis)

*   **Overview:** An end-to-end business intelligence project analyzing retail sales data. I utilized Python for rigorous data cleaning, exploratory data analysis (EDA), and feature engineering, followed by Microsoft Power BI to build interactive, dynamic dashboards for stakeholder reporting.
*   **Top Insights:**
    *   **Profitability vs. Volume:** High sales volume does not inherently guarantee high profitability; specific product sub-categories act as "loss leaders" heavily impacted by steep discount strategies.
    *   **Geographic Variances:** Certain regions consistently over-perform in revenue but suffer from supply chain inefficiencies that eat into their overall profit margins.