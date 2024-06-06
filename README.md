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

Data quality and structure are crucial for insightful analysis. The initial phase involved cleaning and transforming the dataset using Python's pandas library. Composite entries in the 'listed_in' column were separated and categorized by splitting and exploding the string values, converting multiple genres into individual records while retaining corresponding data points. Inconsistencies in the 'rating' column were standardized, consolidating various terms like 'NOT RATED' and age-specific ratings into coherent categories to ensure uniformity and accurate representation of content maturity levels, essential for strategic considerations.

A Python script ([dataprep.py](scripts/dataprep.py)) was used to clean and preprocess the data. This involved standardizing ratings and exploding genre listings to facilitate detailed analysis.


## Tableau Dashboard

Using Tableau, a strategic dashboard was created to compare streaming content across Netflix, Prime Video, Disney+, and Hulu. 
[Airlines Analysis Performance Dashboard](https://public.tableau.com/views/BusinessIntelligenceInsightsforStreamingPlatforms/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)). Below is the screenshot of the dashboard:

![alt text][logo1]

[logo1]: dashboard/dashboard1.png "Streaming Platforms Dashboard"

Prime Video leads in volume, while Disney+ offers a more selective range. Pie charts show Prime Video and Netflix have a substantial share of TV shows.

Genre and rating analysis reveal content strategies: Netflix favours international movies and dramas; Prime Video includes drama, comedy, and suspense; Disney+ focuses on family, animation, and action-adventure; Hulu balances drama and comedy with international appeal.


![alt text][logo2]

[logo2]: dashboard/dashboard2.png "Streaming Platforms Dashboard"


Content origins visualization shows the US as a major content hub, with significant contributions from the UK and India, highlighting diverse content-sourcing strategies for a global audience.

The trend of streaming content availability shows exponential growth, peaking in 2019, reflecting increased production and acquisition in a competitive market demanding continuous innovation and expansion.

## Strategic Recommendation

Insights from Salt Productions' dashboard highlight the need for content diversification. While drama and comedy dominate, international offerings are sparse, presenting an opportunity to capture emerging markets and cater to a diverse audience, reducing genre oversaturation.

Data suggests potential in original content within popular genres, appealing to niche markets seeking innovation. Localization strategies can tailor content to regional tastes, enhancing market presence and audience loyalty.

Integrating the strengths of newly acquired platforms—genre specializations and demographics—can create a robust content ecosystem, improving subscriber value and competitive positioning. Expanding Disney+'s focus on family and educational content meets growing demand and demonstrates social responsibility.

Investing in advanced analytics, AI, and machine learning is crucial for predictive insights, optimizing recommendations, and enhancing user experience. Additionally, in-depth user engagement analysis will provide detailed behavioural insights, enabling a personalized content strategy and increasing viewer satisfaction and loyalty.
