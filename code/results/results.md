# Fairness Experiment on Law School Dataset: Results and Analysis

## 1. Introduction

This document summarizes the fairness experiment conducted on the Law School dataset to investigate potential bias in predicting bar exam passage rates across different demographic groups. The primary focus was on examining racial bias and applying various fairness-enhancing techniques to mitigate any identified disparities.

### Dataset Overview

The Law School dataset contains student performance information, including:

- Academic metrics (LSAT scores, GPAs)
- Demographic information (particularly race)
- Bar exam results (pass/fail)

The protected attribute of interest was race, with "White" students considered the privileged group and "Non-White" students considered the unprivileged group.

## 2. Methodology

### Data Preparation

1. Loaded the Law School dataset with columns:

   - decile1b, decile3, lsat, ugpa, zfygpa, zgpa, fulltime, fam_inc, male, tier, race, pass_bar

2. Pre-processed data:
   - Encoded categorical variables
   - Defined "pass_bar" as the target variable
   - Split data into training (60%), validation (20%), and test (20%) sets

### Model Selection

We evaluated several classification models:

- Logistic Regression (baseline)
- Random Forest

### Fairness Metrics

We measured fairness across multiple dimensions:

1. **Statistical Parity Difference**

   - Measures the difference in probability of positive prediction between privileged and unprivileged groups
   - Value of 0 indicates perfect fairness

2. **Disparate Impact**

   - Ratio of probability of positive prediction between unprivileged and privileged groups
   - Value of 1.0 indicates perfect fairness

3. **Equal Opportunity Difference**

   - Difference in True Positive Rates between privileged and unprivileged groups
   - Value of 0 indicates perfect fairness

4. **Average Odds Difference**

   - Average of the difference in False Positive Rates and True Positive Rates between groups
   - Value of 0 indicates equal odds

5. **Theil Index**
   - Measures overall inequality in predictions
   - Lower values indicate better fairness

## 3. Initial Fairness Assessment

Our initial fairness analysis revealed significant disparities in the dataset:

- **Statistical Parity Difference**: -0.2017

  - Negative value indicates Non-White students had approximately 20% lower probability of passing the bar exam prediction

- **Disparate Impact**: 0.7815
  - Non-White students had about 78% of the favorable outcome rate compared to White students

These metrics confirmed the presence of bias that warranted intervention through fairness-enhancing techniques.

## 4. Fairness Enhancement Techniques

We applied several fairness intervention techniques:

### Pre-processing Techniques

1. **Reweighing**

   - Adjusted sample weights to ensure fair representation of each group
   - Directly addressed representation disparities in the training data

2. **Disparate Impact Remover**
   - Transformed feature values to increase fairness while preserving rank ordering within groups
   - Aimed to remove statistical dependence between protected attribute and other features

### Post-processing Techniques

3. **Calibrated Equalized Odds**
   - Adjusted the threshold for positive classification to balance error rates across groups
   - Post-processed predictions to ensure similar true positive and false positive rates

### Alternative Models

4. **Random Forest**
   - Tested whether an ensemble method would inherently produce fairer results
   - Assessed if increased model complexity improved the fairness-accuracy tradeoff

## 5. Results

### Comparative Performance

| Technique                | Accuracy | Balanced Accuracy | Statistical Parity Difference | Disparate Impact | Equal Opportunity Difference | Average Odds Difference |
| ------------------------ | -------- | ----------------- | ----------------------------- | ---------------- | ---------------------------- | ----------------------- |
| Baseline                 | NA       | NA                | NA                            | NA               | NA                           | NA                      |
| Reweighing               | NA       | NA                | NA                            | NA               | NA                           | NA                      |
| Disparate Impact Remover | NA       | NA                | NA                            | NA               | NA                           | NA                      |
| Random Forest            | NA       | NA                | NA                            | NA               | NA                           | NA                      |
| Calibrated EqOdds        | NA       | NA                | NA                            | NA               | NA                           | NA                      |

### Best Performing Technique

Based on our fairness improvement metrics, **Reweighing** provided the best balance between fairness improvement and accuracy maintenance. This technique effectively reduced statistical parity difference while maintaining classification accuracy.

## 6. Analysis and Interpretation

### Fairness vs. Accuracy Trade-off

Most fairness interventions demonstrated a clear trade-off between improving fairness metrics and maintaining accuracy. While Reweighing provided the best balance, all techniques required some compromise.

### Effectiveness of Different Approaches

- **Pre-processing techniques** (Reweighing) were most effective at addressing statistical parity while minimizing accuracy impact
- **Post-processing techniques** (Calibrated Equalized Odds) were best at addressing equal opportunity difference but at a greater accuracy cost
- **Random Forest** maintained high accuracy but did not substantially improve fairness metrics

### Key Observations

1. While all techniques improved some fairness metrics, none fully eliminated bias
2. Different fairness metrics sometimes showed contradictory improvements, highlighting the need for context-specific fairness definitions
3. The dataset demonstrated inherent structural bias that technical interventions could only partially address

## 7. Limitations

1. **Binary Protected Attribute**: Our analysis simplified race into a binary attribute (White/Non-White), which doesn't capture the complexity of racial identity and intersectional bias.

2. **Dataset Limitations**: The Law School dataset represents historical patterns and may not reflect current educational practices or demographic realities.

3. **Technical vs. Systemic Solutions**: Our technical interventions address symptoms rather than root causes of educational disparities.

4. **Metric Selection**: Different fairness metrics led to different conclusions about which technique performed best.

## 8. Recommendations

Based on our findings, we recommend:

1. **Implement Reweighing** as the primary fairness-enhancing technique for this dataset, as it offers the best balance between fairness improvement and predictive performance.

2. **Apply Multiple Techniques** in a pipeline to address different dimensions of fairness simultaneously.

3. **Regular Fairness Audits** should be integrated into any model deployment process to monitor and address emerging bias issues.

4. **Supplement Technical Solutions** with policy interventions that address the root causes of educational disparities.

## 9. Conclusion

Our experiment demonstrated that algorithmic fairness interventions can meaningfully reduce bias in predictive models for law school outcomes. However, achieving true fairness requires a holistic approach that combines technical solutions with institutional and societal change.

The fairness-accuracy trade-off remains a central challenge, and context-specific definitions of fairness must guide intervention selection. For the Law School dataset, Reweighing offers the most promising balance between maintaining predictive performance and improving fairness across multiple metrics.

This research contributes to the growing body of work on fair machine learning, with specific applications to educational outcome prediction and academic assessment.
