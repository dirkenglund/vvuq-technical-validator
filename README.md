# VVUQ Technical Validator

**Validation, Verification, and Uncertainty Quantification for scientific content.**

A Claude Code plugin that rigorously checks mathematical equations, physics derivations, and engineering calculations for errors.

## Installation

```bash
claude plugin install github:dirkenglund/vvuq-technical-validator
```

## Commands

### `/validate [content]`
Validate a single equation, derivation, or technical claim.

```
/validate "The Heisenberg uncertainty principle: ΔxΔp ≥ ℏ"
```

### `/validate-paper [file]`
Review a scientific paper or section for technical errors.

```
/validate-paper paper.pdf --section methods
```

### `/vvuq-benchmark [suite]`
Run the benchmark suite to test validation accuracy.

```
/vvuq-benchmark papers
```

## What It Checks

### Verification (V1) - Calculation Correctness
- Algebraic manipulations
- Sign errors and factor mistakes
- Limits and boundary conditions

### Validation (V2) - Physical Correctness
- Dimensional analysis
- Conservation laws (energy, momentum, charge)
- Limiting cases
- Physical bounds

### Uncertainty Quantification (UQ)
- Error propagation
- Significant figures
- Confidence intervals

## Benchmark Results

Tested on 48 cases across math, physics, and engineering:

| Model | Basic (22) | Papers (26) | Combined |
|-------|------------|-------------|----------|
| Sonnet | 96% F1 | 100% F1 | **98% F1** |
| Haiku | 100% F1 | 80% F1 | 89% F1 |

### Recommendation
- **Education/grading**: Use Haiku (fast, strict on basics)
- **Research review**: Use Sonnet (better on nuanced physics)
- **Critical applications**: Use both, flag disagreements

## Domains Covered

- **Mathematics**: Calculus, algebra, Fourier analysis, error propagation
- **Physics**: Quantum mechanics, thermodynamics, electromagnetism
- **Electrical Engineering**: Circuits, RF/microwave, signal processing
- **Quantum Optics**: Cavity QED, NV centers, cooperativity
- **Numerical Methods**: Finite differences, FDTD, stability conditions

## Common Errors Detected

| Error Type | Example |
|------------|---------|
| Sign errors | Missing negative in quadratic formula |
| Factor errors | √π vs π, ℏ/2 vs ℏ |
| Dimensional errors | Energy vs momentum (missing v²) |
| Unit errors | Celsius vs Kelvin in thermodynamics |
| Scaling errors | N² vs N (Heisenberg limit) |
| Formula inversions | V=IR vs V=I/R |
| Convention errors | RMS vs peak, cross vs dot product |

## Configuration

In `plugin.json`:

```json
{
  "default_model": "sonnet",
  "strictness": "permissive",
  "domains": ["math", "physics", "electrical_engineering"]
}
```

- **default_model**: `haiku` | `sonnet` | `opus`
- **strictness**: `strict` (flags conventions) | `permissive` (accepts alternatives)
- **domains**: Which domains to check

## License

MIT

## Author

Dirk Englund (@dirkenglund)

Built with Claude Code.
