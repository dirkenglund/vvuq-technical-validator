---
description: Review a scientific paper or section for technical errors
arguments:
  - name: file
    description: Path to the paper (PDF, markdown, or text file)
    required: false
  - name: section
    description: Specific section to focus on (e.g., "methods", "results", "equations")
    required: false
---

# Scientific Paper VVUQ Review

You are conducting a rigorous technical review of a scientific paper using VVUQ methodology.

## Input

$ARGUMENTS

If no file provided, ask the user to paste the paper section or provide a file path.

## Review Checklist

### Equations & Derivations
- [ ] All equations dimensionally consistent
- [ ] Derivation steps follow logically
- [ ] No sign errors or missing factors
- [ ] Limiting cases correctly stated
- [ ] Numerical values plausible

### Physics & Domain Knowledge
- [ ] Conservation laws respected
- [ ] Physical bounds reasonable
- [ ] Approximations valid for stated regime
- [ ] No violations of fundamental limits (Heisenberg, thermodynamics, etc.)

### Uncertainty & Statistics
- [ ] Error propagation correct
- [ ] Significant figures appropriate
- [ ] Confidence intervals properly stated
- [ ] Statistical methods appropriate

### Common Errors to Watch For
- N vs N² scaling (Heisenberg limit)
- Missing factors of 2, π, or √2
- Celsius vs Kelvin in thermodynamics
- RMS vs peak values
- Wrong sign in exponentials (decay vs growth)
- Inverted formulas (V=IR vs V=I/R)
- Cross product vs dot product

## Output Format

```markdown
## Paper Review: [Title/Section]

### Overall Assessment
- **Technical Soundness**: ✅ Sound | ⚠️ Minor Issues | ❌ Major Issues
- **Equations Checked**: X of Y
- **Issues Found**: N (C critical, M major, m minor)

### Detailed Findings

#### Equation/Claim 1
- **Location**: Page X, Eq. Y
- **Status**: PASS | FAIL
- **Issue**: [if any]
- **Suggested Fix**: [if needed]

[Continue for each equation/claim]

### Summary
[Overall technical quality assessment]

### Recommendations
1. [Specific corrections needed]
2. [Clarifications suggested]
```

Be thorough but constructive. The goal is to improve the paper's technical accuracy.
