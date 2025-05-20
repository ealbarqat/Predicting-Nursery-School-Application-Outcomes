# Predicting Nursery School Application Outcomes: A Data-Driven Approach

## Project Overview
This project aims to develop a data-driven approach to nursery school admission decisions using machine learning. By analyzing patterns in successful applications and identifying key factors that influence admission outcomes, we help nursery schools make more efficient, objective, and fair decisions.

## Dataset
- **Source**: [UCI Machine Learning Repository - Nursery Dataset](https://archive.ics.uci.edu/ml/datasets/nursery)
- **Size**: 12,960 records
- **Features**: 8 categorical attributes
- **Target**: 1 class variable (admission outcome)
- **Data Quality**: No missing values, well-balanced feature distributions

### Features
1. Parents' occupation (usual, pretentious, great_pret)
2. Nursery quality (proper, less_proper, improper, critical, very_crit)
3. Form completion (complete, completed, incomplete, foster)
4. Number of children (1, 2, 3, more)
5. Housing conditions (convenient, less_conv, critical)
6. Financial status (convenient, inconv)
7. Social status (nonprob, slightly_prob, problematic)
8. Health status (recommended, priority, not_recom)

## Project Structure
```
Project/
├── nursery/                    # Dataset directory
│   └── nursery.data           # Original dataset
├── results/                    # Analysis results
│   ├── analysis_results.txt    # Basic dataset information
│   ├── model_results.txt       # Model performance metrics
│   ├── feature_importance.png  # Feature importance visualization
│   ├── confusion_matrix.png    # Model confusion matrix
│   ├── correlation_heatmap.png # Feature correlation heatmap
│   ├── class_distribution_*.png # Class distribution visualizations
│   └── *_vs_class_stacked.png  # Attribute-class relationship charts
├── nursery_analysis.py         # Main analysis script
├── report_groupL.tex          # LaTeX report
├── nursery_presentation.md    # Presentation outline
└── README.md                  # This file
```

## Analysis Components
1. **Exploratory Data Analysis (EDA)**
   - Data quality assessment
   - Distribution analysis
   - Feature relationships
   - Class imbalance analysis

2. **Data Preparation**
   - Label encoding
   - Train/test split (80/20)
   - Feature scaling

3. **Model Development**
   - Decision Tree classifier
   - Random Forest classifier
   - Feature importance analysis

4. **Model Evaluation**
   - Confusion matrix analysis
   - Classification metrics
   - Model comparison

## Key Findings
1. **Feature Importance**
   - Health status is the most critical factor (30%)
   - Financial and social status are significant predictors
   - Nursery quality shows moderate importance

2. **Model Performance**
   - Decision Tree: 99% accuracy
   - Random Forest: 98% accuracy
   - Strong predictive power for main classes

3. **Class Distribution**
   - Three main classes dominate the dataset
   - Some classes are rare (e.g., "recommend": only 2 cases)
   - Clear patterns in decision-making factors

## Requirements
- Python 3.x
- Required packages:
  ```
  pandas
  numpy
  matplotlib
  seaborn
  scikit-learn
  ```

## Usage
1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python nursery_analysis.py
   ```
4. View results in the `results` directory

## Results
The analysis results are stored in the `results` directory:
- Text files with detailed analysis and model performance
- Visualizations showing data distributions and relationships
- Model evaluation metrics and comparisons

## Future Work
1. Implementation of more advanced models
2. Addressing class imbalance issues
3. Development of fairness metrics
4. Real-world testing and validation
5. Integration with existing admission systems

## Contributors
- GroupL Members

## License
This project is for educational purposes only.

## Acknowledgments
- UCI Machine Learning Repository for the dataset
- Course instructors and materials
- Open-source community for tools and libraries 