---
description: Validate technical content (equations, derivations, claims) using VVUQ methodology
arguments:
  - name: content
    description: The technical content to validate (equation, derivation, or claim)
    required: false
---

# VVUQ Technical Validation

You are performing Validation, Verification, and Uncertainty Quantification (VVUQ) on technical content.

## Input

$ARGUMENTS

If no content provided, ask the user to paste the equation, derivation, or technical claim they want validated.

## Validation Process

### 1. VERIFICATION (V1) - Is the calculation correct?
- Check algebraic manipulations
- Verify no sign errors or factor mistakes
- Confirm limits and boundary conditions

### 2. VALIDATION (V2) - Does it represent reality?
- **Dimensional Analysis**: All terms have consistent units
- **Conservation Laws**: Energy, momentum, charge conserved
- **Limiting Cases**: Reduces to known results
- **Physical Bounds**: Results within reasonable ranges

### 3. UNCERTAINTY QUANTIFICATION (UQ)
- Error propagation correct?
- Confidence bounds stated?
- Approximations identified?

## Output Format

```markdown
## VVUQ Report

### Summary
- **Status**: ✅ PASS | ⚠️ CONCERNS | ❌ FAIL
- **Confidence**: HIGH | MEDIUM | LOW
- **Domain**: [Math | Physics | EE | QM | ...]

### Verification (V1)
[Assessment of calculation correctness]

### Validation (V2)
[Assessment of physical correctness]

### Issues Found
1. [CRITICAL|MAJOR|MINOR]: Description

### Recommendation
[Specific fix or confirmation]
```

Be rigorous but fair. Flag genuine errors, but accept valid alternative conventions.
