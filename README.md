# National Parks Biodiversity Analysis

## Project Overview
Exploratory data analysis of species and conservation status in U.S. National Parks using Python, followed by interactive visual storytelling in Tableau. The goal of this project is to explore species richness, native vs non-native species, taxonomic categories, and species families across parks.

## Core Questions
1. Which parks have the highest and lowest species richness?
2. What is the composition of native vs non-native species across parks?
3. How does biodiversity break down by taxonomic category?
4. Which species families contribute most to overall biodiversity?

## Data Source
- Kaggle: National Parks Species Dataset (https://www.kaggle.com/datasets/umerhaddii/national-park-species-dataset)
    *(cleaned and preprocessed in Python for data analysis)*

## Data Cleaning & EDA
- Cleaned and prepared the dataset in Python
- Handled duplicates, missing values, and standardized column names
- Performed exploratory data analysis (EDA) to understand species diversity, conservation status, and distribution patterns
- Saved the cleaned dataset for Tableau analysis

## Analysis & Visualization
- Built an interactive Tableau dashboard to answer the four core questions
- Charts include bar charts, stacked bars, treemaps, donut charts, and heatmaps
- Applied filters to Tableau project dashboard to allow for more interactive exploration

## Key Insights

Our analysis of species diversity and conservation status across U.S. National Parks revealed several clear patterns:
  
### 1. Species Richness by Park (Core Question 1)
- The top five parks with the highest species counts are **Great Smoky Mountains, Yellowstone, Rocky Mountain, Grand Canyon, and Glacier National Park**.  
- Parks with the lowest species counts include **Bryce Canyon, Acadia, and Zion National Park**.  

### 2. Native vs. Non-Native Species (Core Question 2)
- Most species across parks are **native**, making up approximately **31.8%** of the dataset, while **non-native species represent only 4.17%**.  
- A large portion of species have an **unknown nativeness**, highlighting gaps in the data.  
- Among taxonomic categories, **amphibians have the highest proportion of native species**, while **Acadia National Park shows the highest percentage of non-native species**.  

### 3. Biodiversity by Taxonomic Category (Core Question 3)
- **Insects** are the most numerous category across all parks, indicating that arthropod diversity dominates in terms of species count.  

### 4. Top Species Families (Core Question 4)
- The family **Asteraceae** has the highest number of unique species across parks, making it the most diverse family represented in the dataset.

## Tools Used
- Python (pandas, matplotlib, seaborn) for data cleaning and EDA
- Tableau (Tableau Public) for interactive dashboard visualization

## Tableau Dashboard
Explore the interactive dashboard here:[National Parks Biodiversity Analysis](https://public.tableau.com/views/NationalParksSpeciesAnalysisTableau/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)
