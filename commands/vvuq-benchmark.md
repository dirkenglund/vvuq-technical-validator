---
description: Run VVUQ benchmark suite to test validation accuracy
arguments:
  - name: suite
    description: Benchmark suite to run (basic, papers, all)
    required: false
  - name: cases
    description: Number of cases to run (default all)
    required: false
---

# VVUQ Benchmark Runner

Run the validation benchmark suite to measure VVUQ accuracy.

## Available Suites

- **basic**: 22 textbook-level cases (math, physics, EE)
- **papers**: 26 real paper excerpt cases (quantum optics, solid state, RF, numerical)
- **all**: Complete 48-case benchmark

## Baseline Performance

| Model | Basic (22) | Papers (26) | All (48) |
|-------|------------|-------------|----------|
| Sonnet | 96% F1 | 100% F1 | 98% F1 |
| Haiku | 100% F1 | 80% F1 | 89% F1 |

## Running the Benchmark

$ARGUMENTS

If no suite specified, run a quick 6-case sample.

## Process

1. Load test cases from `benchmarks/test_cases/`
2. Evaluate each case using VVUQ methodology
3. Compare predictions to ground truth
4. Calculate precision, recall, F1, accuracy
5. Report results

## Output

```markdown
## Benchmark Results

### Summary
- Suite: [basic|papers|all]
- Cases: N
- Model: [current model]

### Metrics
| Metric | Value |
|--------|-------|
| Precision | X% |
| Recall | X% |
| F1 Score | X% |
| Accuracy | X% |

### Confusion Matrix
| | Predicted Error | Predicted Correct |
|--|-----------------|-------------------|
| Has Error | TP | FN |
| Is Correct | FP | TN |

### Errors
[List any false positives or false negatives]
```

This benchmark helps calibrate the validator and compare model performance.
