import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('all_data.csv')
df.head()
df.describe(include='all')

df.Country.unique()

df = df.rename(str.lower, axis='columns')
df = df.rename(columns={'life expectancy at birth (years)': 'life_expectancy'})

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
ax1.hist(df.gdp)
ax1.set_title('GDP distribution of dataset')
ax1.set_xlabel('GDP (Trillions in U.S. Dollars)')
ax1.set_ylabel('Frequency')

ax2.hist(df.life_expectancy)
ax2.set_title('Life expectancy distribution of dataset')
ax2.set_xlabel('Age (Years)')
ax2.set_ylabel('Frequency')

plt.show()

df_gdp_mean = df[['country', 'gdp']].copy()
df_gdp_mean.groupby(['country']).mean()

plt.figure(figsize=(15, 5))
sns.barplot(df_gdp_mean, x='country', y='gdp', errorbar=None)
plt.title('Average GDP by Country')
plt.xlabel('GDP (Trillions in USD)')
plt.ylabel('Country')
plt.show()

df_life_mean = df[['country','life_expectancy']].copy()
df_life_mean.groupby(['country']).mean()

plt.figure(figsize=(10, 7))
sns.barplot(df_life_mean, x='life_expectancy', y='country', errorbar=None)
plt.title('Average Life Expectancy by Country')
plt.xlabel('Age (Years)')
plt.ylabel('Country')
plt.show()

sns.violinplot(data=df, x='life_expectancy', y='country', hue='country')
plt.title('Violin Plot of Life Expectancy of Countries')
plt.xlabel('Age (Years)')
plt.ylabel('Country')
plt.show()

sns.lineplot(df, x='year', y='life_expectancy', hue='country')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.title('Life Expectancy vs Year for all countries')
plt.xlabel('Year')
plt.ylabel('Life Expectancy (Year)')
plt.show()

facet_life = sns.FacetGrid(data=df, col='country', hue='country',
                  col_wrap=3, sharey=False)
facet_life.map(sns.lineplot, 'year','life_expectancy').add_legend()
plt.show()


sns.lineplot(df, x='year', y='gdp', hue='country')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.title('GDP vs Year for all Countries')
plt.xlabel('Year')
plt.ylabel('GDP in USD Trillions')
plt.show()

facet_gdp_line = sns.FacetGrid(df, col='country', hue='country',
                               col_wrap=3, sharey=False)
facet_gdp_line.map(sns.lineplot, 'year', 'gdp').add_legend()

plt.show()


facet_gdp_life = sns.FacetGrid(df, col='country', hue='country',
                               col_wrap=3, sharex=False, sharey=False)
facet_gdp_life.map(sns.scatterplot, 'life_expectancy', 'gdp')
plt.show()

