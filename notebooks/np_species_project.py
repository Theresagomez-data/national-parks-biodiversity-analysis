# np_species_project.py
# Portfolio project: Exploring species data from US National Parks
# Goal: Show data cleaning, exploration, and visualization skills while answering key questions about biodiversity

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Step 0: Load dataset


df = pd.read_csv("most_visited_nps_species_data.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Strip spaces in all text columns
text_columns = df.select_dtypes(include='object').columns
for col in text_columns:
    df[col] = df[col].str.strip()

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned dataset for Tableau
df.to_csv("cleaned_nps_species_data.csv", index=False)


# Step 1: Exploratory Analysis / Visualizations


# Figure 1: Species count by park
species_df = df.groupby('parkname')['sciname'].nunique().reset_index()
species_df.columns = ['parkname', 'species_count']

plt.figure(1, figsize=(10,6))
sns.barplot(data=species_df, x='parkname', y='species_count', palette="viridis")
plt.xticks(rotation=45, ha='right')
plt.ylabel("Number of Unique Species")
plt.title("Figure 1: Species Count by Park")
plt.tight_layout()
plt.show()


# Figure 2: Native vs Non-native species per park
if 'nativeness' in df.columns:
    native_df = df.groupby(['parkname','nativeness'])['sciname'].nunique().unstack(fill_value=0)
    native_df['Total'] = native_df.sum(axis=1)
    native_df['Native_percent'] = (native_df.get('Native', 0) / native_df['Total'] * 100)
    native_df['NonNative_percent'] = 100 - native_df['Native_percent']

    # Create a matplotlib figure
    plt.figure(2, figsize=(10,6))
    ax = plt.gca()  # Get current axis

    # Plot on the existing axis
    native_df[['Native_percent','NonNative_percent']].plot(
        kind='bar', stacked=True, colormap='Paired', ax=ax
    )
    plt.ylabel("Percentage of Species")
    plt.title("Figure 2: Native vs Non-native Species by Park")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Figure 3: Species count by category
if 'categoryname' in df.columns:
    category_df = df.groupby('categoryname')['sciname'].nunique().reset_index()
    category_df.columns = ['categoryname', 'species_count']

    plt.figure(3, figsize=(8,6))
    sns.barplot(data=category_df, x='categoryname', y='species_count', palette="magma")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Number of Unique Species")
    plt.title("Figure 3: Species Count by Category")
    plt.tight_layout()
    plt.show()

# Figure 4: Top 10 families by species count
if 'family' in df.columns:
    family_df = df.groupby('family')['sciname'].nunique().reset_index()
    family_df.columns = ['family', 'species_count']
    top10_families = family_df.sort_values('species_count', ascending=False).head(10)

    plt.figure(4, figsize=(10,6))
    sns.barplot(data=top10_families, x='family', y='species_count', palette="coolwarm")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Number of Unique Species")
    plt.title("Figure 4: Top 10 Families by Species Count")
    plt.tight_layout()
    plt.show()


# Step 2: Insights / Story


# - Core Question 1 (Species per park): Some parks show significantly higher recorded species richness than others.
#   In this dataset, Great Smoky Mountains National Park has the highest number of unique species, while Bryce Canyon National Park has the lowest. 
#   These differences likely reflect ecological factors, habitat diversity, and variation in survey effort across parks.
# - Core Question 2 (Native vs Non-native): Most species across all parks are native, with a smaller proportion being non-native. 
#   Great Smoky Mountains shows the highest proportion of non-native species among parks.
# - Core Question 3 (Species by category): Across all parks, insects and vascular plants have the highest number of unique species, 
#   while amphibians have the fewest.
# - Core Question 4 (Family-level insights): Within plants, the family Asteraceae has the highest number of unique species, while within insects, 
#   Carabidae has the lowest, highlighting differences in diversity among taxonomic groups.
# - These insights can help prioritize which taxonomic groups may need more detailed monitoring and conservation efforts across various National Parks.
# - Note: Observed species counts may reflect survey effort differences, not absolute biodiversity.
# - Skills showcased: Python for data cleaning, aggregation, and visualization to uncover ecological patterns.