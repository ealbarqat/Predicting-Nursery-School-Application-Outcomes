import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
import io
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Read the data
columns = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'class']
df = pd.read_csv('nursery/nursery.data', names=columns)

# Create a results directory if it doesn't exist
import os
if not os.path.exists('results'):
    os.makedirs('results')

# 1. Basic Data Analysis
print("Dataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Save basic information
with open('results/analysis_results.txt', 'w') as f:
    f.write("Nursery Dataset Analysis\n")
    f.write("=======================\n\n")
    f.write(f"Dataset Shape: {df.shape}\n")
    
    # Get DataFrame info as string
    buffer = io.StringIO()
    df.info(buf=buffer, max_cols=None, show_counts=True)
    f.write("\nColumn Information:\n")
    f.write(buffer.getvalue())
    
    f.write("\n\nMissing Values:\n")
    f.write(str(df.isnull().sum()))
    
    # Add value counts for each categorical column
    f.write("\n\nValue Counts for Each Column:\n")
    for column in df.columns:
        f.write(f"\n{column}:\n")
        f.write(str(df[column].value_counts()))
        f.write("\n")

# 2. Data Preparation
# Encode categorical variables
le = LabelEncoder()
df_encoded = df.copy()
for column in df.columns:
    df_encoded[column] = le.fit_transform(df[column])

# Prepare features and target
X = df_encoded.drop('class', axis=1)
y = df_encoded['class']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Visualizations
# 3.1 Class Distribution (Bar Chart)
plt.figure(figsize=(12, 6))
class_counts = df['class'].value_counts()
sns.barplot(x=class_counts.index, y=class_counts.values)
plt.title('Distribution of Nursery Application Outcomes')
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/class_distribution_bar.png')

# 3.2 Pie Chart for Class Proportions
plt.figure(figsize=(10, 10))
plt.pie(class_counts.values, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Proportion of Nursery Application Outcomes')
plt.axis('equal')
plt.tight_layout()
plt.savefig('results/class_distribution_pie.png')

# 3.3 Stacked Bar Charts for each attribute vs class
for column in df.columns[:-1]:  # Exclude the target column
    plt.figure(figsize=(12, 6))
    cross_tab = pd.crosstab(df[column], df['class'])
    cross_tab.plot(kind='bar', stacked=True)
    plt.title(f'Relationship between {column} and Class')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'results/{column}_vs_class_stacked.png')

# 3.4 Decision Tree Visualization
# Train Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

# Create confusion matrix for Decision Tree
plt.figure(figsize=(10, 8))
cm_dt = confusion_matrix(y_test, dt_pred)
sns.heatmap(cm_dt, 
            annot=True, 
            fmt='d', 
            cmap='Blues',
            xticklabels=le.classes_,
            yticklabels=le.classes_)
plt.title('Confusion Matrix - Decision Tree')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('results/confusion_matrix_decision_tree.png')

# Visualize the full Decision Tree
plt.figure(figsize=(20,10))
plot_tree(dt_model, 
          feature_names=X.columns,
          class_names=le.classes_,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('Decision Tree Visualization (Full Model)')
plt.tight_layout()
plt.savefig('results/decision_tree_viz.png')

# 3.5 Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation = df_encoded.corr()
sns.heatmap(correlation, 
            annot=True, 
            cmap='coolwarm', 
            fmt='.2f',
            square=True,
            linewidths=.5,
            cbar_kws={"shrink": .8})
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.savefig('results/correlation_heatmap.png')

# 4. Model Building and Evaluation
# Train Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Create confusion matrix for Random Forest
plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_test, rf_pred)
sns.heatmap(cm, 
            annot=True, 
            fmt='d', 
            cmap='Blues',
            xticklabels=le.classes_,
            yticklabels=le.classes_)
plt.title('Confusion Matrix - Random Forest')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('results/confusion_matrix.png')

# Save model results
with open('results/model_results.txt', 'w') as f:
    f.write("Model Performance Results\n")
    f.write("=======================\n\n")
    
    f.write("Decision Tree Results:\n")
    f.write(classification_report(y_test, dt_pred))
    f.write("\n\nRandom Forest Results:\n")
    f.write(classification_report(y_test, rf_pred))

# 5. Feature Importance
plt.figure(figsize=(12, 6))
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
})
feature_importance = feature_importance.sort_values('importance', ascending=False)
sns.barplot(data=feature_importance, x='importance', y='feature')
plt.title('Feature Importance (Random Forest)')
plt.tight_layout()
plt.savefig('results/feature_importance.png')

print("\nAnalysis complete! Results have been saved in the 'results' directory.") 