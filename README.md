# Business Intelligence Insights for Streaming Platforms
This repository contains a project for analyzing and visualizing content on major streaming platforms (Netflix, Prime Video, Disney+, and Hulu). The project includes data preparation, visualization, and strategic analysis to support Salt Productions in identifying new opportunities and enhancing its business intelligence (BI) strategy.

## Project Background

Salt Productions, the largest television production company in the Northern Hemisphere, has recently acquired HBO, Netflix, Comedy Central, and other major television producers. This acquisition has prompted the need to integrate data across these new assets and develop a robust data analytics strategy. As part of a team from Business Intelligence Consultants, you have been hired to draft a detailed report for stakeholders, proposing an analytics strategy and analysing the streaming platforms' dataset.

## Objectives

- Define Business Intelligence (BI) and outline its key elements.
- Conduct a preliminary investigation into the streaming platform industry and identify current trends.
- Propose appropriate tools and techniques for future analyses.
- Create a dashboard and visualize the streaming platforms dataset using Tableau.
- Present key findings and provide strategic recommendations to stakeholders.

## Data

The data used in this project includes listings of all the movies and TV shows available on four major streaming platforms, along with details such as cast, directors, ratings, release year, and duration.

- `netflix_titles.csv`: Information about Netflix titles.
- `amazon_prime_titles.csv`: Information about Amazon Prime Video titles.
- `disney_plus_titles.csv`: Information about Disney+ titles.
- `hulu_titles.csv`: Information about Hulu titles.

## Dashboard Creation
The construction of a Tableau-based dashboard for Salt Productions is an exercise in transforming copious amounts of raw data into a coherent narrative that facilitates strategic decision-making. Tableau's acclaimed visualization capabilities render an interactive and user-friendly experience, transforming complex data from diverse streaming platforms into a structured and visually engaging summary. This dashboard is carefully designed to prevent cognitive overload by presenting data in a format that accelerates comprehension and supports efficient analysis.
The dashboard aims to answer several business questions:
- How does the content distribution across different streaming platforms compare?
- What are the prevalent genres on each platform, and what does this imply about their content strategies?
- Where does the content originate from, and how does this reflect on the global content strategy?
- How has the availability of streaming content evolved? 
By addressing these questions, the dashboard serves as a decision-support tool, providing critical insights into content distribution and genre prevalence across streaming platforms, which informs Salt Productions' content strategy alignment and identification of market gaps. By revealing the geographic origin of content, it helps strategize for global market penetration, while the analysis of content evolution aids in forecasting industry trends to pinpoint new opportunities for future projects.



## Data Preparation

A Python script ([dataprep.py](scripts/dataprep.py)) was used to clean and preprocess the data. This involved standardizing ratings and exploding genre listings to facilitate detailed analysis.


## Tableau Dashboard

The following dashboard was created to visualize the streaming platforms' data. (Tableau public dashboard viz link 
[Airlines Analysis Performance Dashboard](https://public.tableau.com/views/BusinessIntelligenceInsightsforStreamingPlatforms/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)). Below is the screenshot of the dashboard:

![alt text][logo1]

[logo1]: dashboard/dashboard1.png "Streaming Platforms Dashboard"

![alt text][logo2]

[logo2]: dashboard/dashboard2.png "Streaming Platforms Dashboard"

## Global Streaming Content Origins

This dashboard illustrates the origin of streaming content across different platforms, highlighting the leading countries in content production.


