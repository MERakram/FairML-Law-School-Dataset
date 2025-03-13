# Investigating and Mitigating Bias in Law School Bar Exam Predictions

## 1. Introduction & Research Question

- **Problem Statement**: Algorithmic bias in educational predictions affects opportunities and outcomes
- **Motivation**: ML systems increasingly impact educational and career trajectories
- **Research Question**: How can we detect and mitigate racial bias in bar exam passage predictions?
- **Project Goals**:
  - Measure existing bias in predictions
  - Implement and compare fairness-enhancing techniques
  - Provide recommendations for fair prediction systems
- **Visual**: Diagram showing bias entry points in prediction pipeline

## 2. Dataset & Problem Overview

- **Law School Dataset**:
  - Features: LSAT scores, GPAs, demographic information
  - Target: Bar exam passage (pass/fail)
  - Protected attribute: Race (White vs. Non-White)
- **Dataset Structure**:
  - 12 columns: decile1b, decile3, lsat, ugpa, zfygpa, zgpa, fulltime, fam_inc, male, tier, race, pass_bar
  - Categorical and numerical features
- **Fairness Definition**: Equal opportunity regardless of race
- **Visual**: Histogram comparing pass rates between demographic groups

## 3. Fairness Metrics & Methodology

- **Fairness Metrics Explained**:
  - **Statistical Parity Difference**: Equality of positive prediction rates
  - **Disparate Impact**: Ratio of favorable outcomes between groups
  - **Equal Opportunity Difference**: Equality of true positive rates
  - **Average Odds Difference**: Balance in error rates across groups
  - **Theil Index**: Overall inequality in predictions
- **Methodology Workflow**:
  1. Data preparation and encoding
  2. Baseline model training
  3. Initial fairness assessment
  4. Application of fairness techniques
  5. Comparative evaluation
- **Visual**: Diagram of fairness evaluation framework and metrics

## 4. Initial Fairness Assessment

- **Baseline Model**: Logistic Regression
- **Performance Metrics**:
  - Accuracy: 90.16%
  - Balanced Accuracy: 61.51%
- **Fairness Metrics**:
  - Statistical Parity Difference: -0.2017
  - Disparate Impact: 0.7815
  - Equal Opportunity Difference: -0.1004
- **Interpretation**:
  - Non-White students had 20% lower probability of positive predictions
  - Non-White students received favorable outcomes at only 78% the rate of White students
- **Visual**: Bar chart comparing initial metrics to "fair" values

## 5. Bias Mitigation Techniques

- **Pre-processing Techniques**:
  - **Reweighing**:
    - How it works: Adjusts training instance weights to ensure fairness
    - Implementation: AIF360 Reweighing algorithm
  - **Disparate Impact Remover**:
    - How it works: Transforms features to increase fairness while preserving ranking
    - Implementation: Repair level set to 0.8
- **Post-processing Techniques**:
  - **Calibrated Equalized Odds**:
    - How it works: Adjusts probability thresholds to equalize error rates
    - Implementation: Uses validation set for threshold optimization
- **Alternative Models**:
  - **Random Forest**: Ensemble method to test if model complexity affects fairness
- **Visual**: Flowchart of ML pipeline with intervention points highlighted

## 6. Comparative Results

- **Performance Table**:

  | Technique              | Accuracy | Statistical Parity Diff | Disparate Impact | Equal Opportunity Diff |
  | ---------------------- | -------- | ----------------------- | ---------------- | ---------------------- |
  | Baseline               | 0.9016   | -0.1982                 | 0.7993           | -0.1004                |
  | Reweighing             | 0.9016   | -0.1318                 | 0.8661           | -0.0875                |
  | DisparateImpactRemover | 0.9017   | -0.2009                 | 0.7966           | -0.0932                |
  | RandomForest           | 1.0000   | -0.2017                 | 0.7815           | -0.0952                |
  | CalibratedEqOdds       | 0.8964   | -0.2085                 | 0.7915           | -0.0241                |

- **Key Improvements**:
  - Reweighing: 33% improvement in statistical parity with minimal accuracy impact
  - Calibrated EqOdds: 76% improvement in equal opportunity but with accuracy cost
- **Visual**: Multi-panel chart showing fairness-accuracy trade-offs

## 7. Key Insights & Analysis

- **Effectiveness by Technique Type**:
  - Pre-processing techniques best for statistical parity
  - Post-processing techniques best for equal opportunity
  - Alternative models maintained accuracy but didn't improve fairness
- **Key Observations**:
  - No technique completely eliminated bias
  - Different metrics sometimes gave contradictory assessments
  - Technical interventions address symptoms not root causes
- **Trade-off Analysis**: Most fairness improvements came with accuracy costs
- **Visual**: Decision matrix for selecting appropriate techniques based on fairness priorities

## 8. Recommendations & Implementation

- **Primary Recommendation**: Implement Reweighing as the main fairness technique
- **Supporting Evidence**: Best balance of fairness improvement and accuracy maintenance
- **Implementation Strategy**:
  1. Apply multiple techniques in combination
  2. Integrate regular fairness audits into model monitoring
  3. Define context-specific fairness criteria
  4. Supplement technical solutions with policy changes
- **Visual**: Implementation roadmap with decision points

## 9. Limitations & Future Work

- **Current Limitations**:
  - Binary protected attribute oversimplifies race
  - Historical dataset may not reflect current realities
  - Limited to available features - missing important context
  - Only considered supervised classification techniques
- **Future Directions**:
  - Intersectional fairness (race × gender × socioeconomic status)
  - Causal models for fairness
  - Exploration of newer fairness metrics and techniques
- **Visual**: Research roadmap showing next steps

## 10. Conclusion

- **Summary of Findings**:
  - Significant bias exists in bar exam predictions
  - Reweighing offers best fairness-accuracy balance
  - Multiple fairness dimensions require multiple approaches
- **Broader Implications**:
  - Educational predictions need fairness-aware approaches
  - Technical solutions only part of comprehensive fairness strategy
  - Context-specific definitions of fairness are essential
- **Final Thought**: "Fair machine learning isn't just about algorithms—it's about creating systems that expand opportunity rather than reinforce historical patterns of disadvantage."
- **Visual**: Key takeaways and contact information

## Notes for Presenter

- Allocate 25-30 minutes for presentation, 5-10 minutes for questions
- Prepare explanations of fairness metrics for non-technical audience
- Be ready to discuss real-world implications of the fairness-accuracy trade-off
- Consider having interactive elements showing how fairness interventions work
