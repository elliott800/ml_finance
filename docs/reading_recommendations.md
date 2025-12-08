# Reading Recommendations

A curated list of books suggested for this project. See each title for further reading on finance, trading systems, and
machine learning applied to finance.

## Table of contents

- [Recommended Books](#recommended-books)
- [Grouped By Category & Reading Priority](#grouped-by-category--reading-priority)
- [Start Here — Recommended Reading Path](#start-here)
- [Annotations & Quick References](#annotations--quick-references)

## Recommended Books

| Title                                                   | Author                  | Year | Category              | ISBN-13       |
| ------------------------------------------------------- | ----------------------- | ---: | --------------------- | ------------- |
| [Advances In Financial Machine Learning](#afml)         | M. López de Prado       | 2018 | ML & Data             | 9781119482109 |
| [Algorithmic And High Frequency Trading](#cartea)       | Á. Cartea et al.        | 2015 | Market Microstructure | 9781107091146 |
| [High Frequency Trading](#aldridge)                     | I. Aldridge             | 2013 | Market Microstructure | 9781118434017 |
| [Inside The Black Box](#narang)                         | R. Narang               | 2009 | Trading Systems       | 9780470432068 |
| [Intermarket Trading Strategies](#katsanos)             | M. Katsanos             | 2008 | Trading Systems       | 9780470758106 |
| [Investment Banking](#rosenbaum)                        | J. Rosenbaum & J. Pearl | 2013 | Finance               | 9781118421611 |
| [Mastering Pandas For Finance](#pandas)                 | M. Heydt                | 2015 | ML & Data             | 9781783985104 |
| [Machine Learning For Algorithmic Trading](#jansen)     | S. Jansen               | 2018 | ML & Data             | 9781839217715 |
| [Options As A Strategic Investment](#mcmillan)         | L. G. McMillan          | 1980 | Derivatives           | 9780735204652 |
| [Systematic Trading](#carver)                           | R. Carver               | 2015 | Trading Systems       | 9780857194459 |
| [Time Series Analysis: Forecasting And Control](#boxjenkins) | Box et al.              | 1976 | Time Series           | 9780470272848 |
| [Trading Systems and Methods](#kaufman)                 | P. Kaufman              | 2013 | Trading Systems       | 9781118043561 |
| [Trading Systems: New Approach To Portfolio Optimisation](#jaekle) | Tomasini & Jaekle       | 2009 | Trading Systems       | 9781905641796 |

---

## Grouped By Category & Reading Priority

- **ML & Data (Priority: High)**

  - `Advances In Financial Machine Learning` — essential for ML best-practices in finance. (Est. read time: 15h)
  - `Machine Learning For Algorithmic Trading` — hands-on implementation and pipelines. (Est. read time: 12h)
  - `Mastering Pandas For Finance` — practical data engineering patterns for time series. (Est. read time: 8h)

- **Trading Systems & Portfolio (Priority: Medium)**n
  - `Systematic Trading` — portfolio-level thinking and risk budgeting. (Est. read time: 6h)
  - `Trading Systems and Methods` — catalog of systems and indicators for hypothesis testing. (Est. read time: 10h)
  - `Trading Systems: New Approach To Portfolio Optimisation` — practical strategy combination and allocation. (Est.
    read time: 8h)
  - `Inside The Black Box` — industry context and strategy taxonomy. (Est. read time: 6h)

- **Market Microstructure & Execution (Priority: Medium-High)**

  - `Algorithmic And High Frequency Trading` — formal execution models and transaction costs. (Est. read time: 12h)
  - `High Frequency Trading` — operational constraints and HFT engineering. (Est. read time: 9h)

- **Quantitative Finance & Time Series (Priority: Medium)**

  - `Time Series Analysis: Forecasting And Control` — classical statistical forecasting foundation. (Est. read time:
    16h)

- **Derivatives & Instrument-specific (Priority: Low-Medium)**

  - `Options As A Strategic Investment` — comprehensive options strategies and risk management. (Est. read time: 12h)

- **Corporate & Event-driven (Priority: Low)**
  - `Investment Banking` — valuation and corporate event mechanics useful for event-driven ideas. (Est. read time: 7h)

## Start Here

A suggested short path for contributors getting up to speed quickly. Click a title to jump to its annotation.

1. [Advances In Financial Machine Learning](#afml) (15h) — Read selective chapters (data issues, labeling, model
   selection) to learn ML hygiene specific to finance.
2. [Machine Learning For Algorithmic Trading](#jansen) (12h) — Follow the end-to-end examples to see how pipelines are
   built and deployed.
3. [Mastering Pandas For Finance](#pandas) (8h) — Implement core ETL and feature-engineering patterns used in the repo.
4. [Systematic Trading](#carver) (6h) — Learn portfolio-level constraints and risk management that will influence
   strategy sizing.
5. [Trading Systems and Methods](#kaufman) (10h) — Use as a reference to prototype baseline systems and indicators.

This path focuses on practical ML/data hygiene first, then system prototyping and portfolio constraints.

> Note on estimated read times: these are approximate and assume a technical reading speed (~30–50 pages/hour) plus time
> for code examples or exercises — treat them as rough guidance rather than strict commitments.

---

## Annotations & Quick References

### Advances In Financial Machine Learning — Marcos López de Prado (2018)

- [OpenLibrary](https://openlibrary.org/works/OL27686638W) | [Goodreads](https://www.goodreads.com/book/isbn/9781119482109)
- **Est. read time:** 15h
- **Recommended chapters:** Chapter 1 (Financial Data Structures), Chapter 4 (Sampling and Labeling), Chapter 6 (Model Selection and Backtesting)
- **Quick notes:** Focus on event-based labeling, fractional differentiation, and purged cross-validation.
- **Why this matters for the repo:** Guides the correct way to label data, validate models, and avoid backtest overfitting — directly applicable to model evaluation and pipeline hygiene. The book balances mathematical intuition with runnable pseudocode and practical case studies for defensible research.
- **Exercise:** Implement a minimal event-based labeler and a purged K-fold CV wrapper using a small sample price series; add tests that demonstrate label alignment and leakage protection.

### Machine Learning For Algorithmic Trading — Stefan Jansen (2018)

- [OpenLibrary](https://openlibrary.org/works/OL25188681W) | [Goodreads](https://www.goodreads.com/book/isbn/9781839217715)
- **Est. read time:** 12h
- **Recommended chapters:** Data acquisition & sources, Feature engineering sections, Model evaluation and deployment
- **Quick notes:** Code-oriented end-to-end examples for building ML pipelines and integrating alternative data.
- **Why this matters for the repo:** Provides reproducible patterns and concrete implementation examples that can be adapted for our ETL and model training code; emphasizes reproducibility and deployment.
- **Exercise:** Recreate one of the book's feature pipelines on a provided sample CSV and produce a small end-to-end training script that outputs cross-validated metrics.

### Mastering Pandas For Finance — Michael Heydt (2015)

- [OpenLibrary](https://openlibrary.org/works/OL27686638W) | [Goodreads](https://www.goodreads.com/book/isbn/9781783985104)
- **Est. read time:** 8h
- **Recommended chapters:** Time series basics and indexing, Efficient window functions, ETL and pipeline patterns
- **Quick notes:** Practical tips for performance and organization of time-series DataFrames; covers resampling, window functions and efficient rolling calculations.
- **Why this matters for the repo:** Helps standardize data shaping and efficient feature computation used across backtests and live pipelines.
- **Exercise:** Implement a small set of optimized rolling feature functions (mean, std, z-score) and benchmark them vs naive implementations on a multi-year sample.

### Algorithmic And High Frequency Trading — Álvaro Cartea, Sebastian Jaimungal, José Penalva (2015)

- [OpenLibrary](https://openlibrary.org/works/OL25047296W) | [Goodreads](https://www.goodreads.com/book/isbn/9781107091146)
- **Est. read time:** 12h
- **Recommended chapters:** Execution strategies, Market impact models, Market making formulations
- **Quick notes:** Mathematical models for optimal execution and cost-aware trading.
- **Why this matters for the repo:** Informs execution-aware strategy design, slippage modelling, and cost-sensitive backtests.
- **Exercise:** Implement a simple VWAP/slippage simulation that evaluates cost under varying participation rates and spreads.

### Trading Systems and Methods — Perry Kaufman (2013)

- [OpenLibrary](https://openlibrary.org/works/OL1904515W) | [Goodreads](https://www.goodreads.com/book/isbn/9781118043561)
- **Est. read time:** 10h
- **Recommended chapters:** System examples, Indicator descriptions, Position sizing and money management
- **Quick notes:** Catalog of techniques and system testing guidance; emphasizes robust evaluation and money management.
- **Why this matters for the repo:** Source of baseline systems and diagnostics to quickly prototype and sanity-check strategies.
- **Exercise:** Pick one indicator from the book, implement it, and run a vectorized backtest over sample data; report drawdown and Sharpe.

### Systematic Trading — Robert Carver (2015)

- [OpenLibrary](https://openlibrary.org/works/OL21715813W) | [Goodreads](https://www.goodreads.com/book/isbn/9780857194459)
- **Est. read time:** 6h
- **Recommended chapters:** Risk budgeting, Sizing and stress-testing, Implementation constraints
- **Quick notes:** Emphasizes pragmatic robustness and portfolio-level considerations.
- **Why this matters for the repo:** Shapes portfolio-level decisions and risk controls used in our sizing and aggregation logic.
- **Exercise:** Create a simple risk-budgeted position sizing function and simulate its effect on a set of synthetic strategy returns.

### Inside The Black Box — Rishi K. Narang (2009)

- [OpenLibrary](https://openlibrary.org/works/OL13773464W) | [Goodreads](https://www.goodreads.com/book/isbn/9780470432068)
- **Est. read time:** 6h
- **Recommended chapters:** Strategy taxonomies, Risk and operational controls
- **Quick notes:** Context on professional quant operations and strategy validation.
- **Why this matters for the repo:** Helps align research workflows and validation expectations with industry practice.
- **Exercise:** Draft a one-page strategy validation checklist inspired by the book and apply it to an existing example strategy in the repo.

### Intermarket Trading Strategies — Markos Katsanos (2008)

- [OpenLibrary](https://openlibrary.org/works/OL13609400W) | [Goodreads](https://www.goodreads.com/book/isbn/9780470758106)
- **Est. read time:** 7h
- **Recommended chapters:** Cross-market indicators, Examples of intermarket rules
- **Quick notes:** Useful for multi-market signal design and correlation handling.
- **Why this matters for the repo:** Applicable when adding cross-asset signals or regime-aware features.
- **Exercise:** Build a simple intermarket feature (e.g., equity vs commodity ratio) and evaluate its predictive value on target returns.

### Investment Banking — Joshua Rosenbaum & Joshua Pearl (2013)

- [OpenLibrary](https://openlibrary.org/works/OL20592402W) | [Goodreads](https://www.goodreads.com/book/isbn/9781118421611)
- **Est. read time:** 7h
- **Recommended chapters:** Comparable company analysis, DCF basics, Deal process overview
- **Quick notes:** Valuation and deal mechanics useful for event-driven ideas.
- **Why this matters for the repo:** Provides templates for translating corporate events into event-driven signals.
- **Exercise:** Create a simple event-driven signal extractor that flags earnings surprises from a CSV of reported vs consensus EPS.

### Options As A Strategic Investment — Lawrence G. McMillan (1980)

- [OpenLibrary](https://openlibrary.org/works/OL266290W) | [Goodreads](https://www.goodreads.com/book/isbn/9780735204652)
- **Est. read time:** 12h
- **Recommended chapters:** Option strategies catalog, Volatility trading and Greeks
- **Quick notes:** Extensive options strategy reference and volatility concepts.
- **Why this matters for the repo:** Necessary reference when designing options hedges or multi-leg experiments.
- **Exercise:** Implement payoff diagrams for a set of basic option strategies and simulate P&L across spot/volatility scenarios.

### Time Series Analysis: Forecasting And Control — Box, Jenkins, Reinsel (1976)

- [OpenLibrary](https://openlibrary.org/works/OL2181533W) | [Goodreads](https://www.goodreads.com/book/isbn/9780470272848)
- **Est. read time:** 16h
- **Recommended chapters:** ARIMA modelling, Model identification and diagnostics
- **Quick notes:** Classical foundation for ARIMA and diagnostic checks.
- **Why this matters for the repo:** Provides interpretable, statistically-grounded methods complementary to ML approaches.
- **Exercise:** Fit a small ARIMA model to a sample series and compare its residual diagnostics to a simple ML baseline.

### Trading Systems: New Approach To Portfolio Optimisation — Urban Jaekle & Emilio Tomasini (2009)

- [OpenLibrary](https://openlibrary.org/works/OL16917793W) | [Goodreads](https://www.goodreads.com/book/isbn/9781905641796)
- **Est. read time:** 8h
- **Recommended chapters:** Combining systems, Robustness measures, Allocation techniques
- **Quick notes:** Practical methods to combine strategies and control drawdown concentration.
- **Why this matters for the repo:** Useful when building multi-strategy portfolios and allocation rules.
- **Exercise:** Implement a simple robustness-weighted ensemble where strategy weights are scaled by a rolling Sharpe stability measure.

### High Frequency Trading — Irene Aldridge (2013)

- [OpenLibrary](https://openlibrary.org/works/OL21429233W) | [Goodreads](https://www.goodreads.com/book/isbn/9781118434017)
- **Est. read time:** 9h
- **Recommended chapters:** Market making and latency, HFT infrastructure, Execution considerations
- **Quick notes:** Operational and engineering constraints for low-latency trading.
- **Why this matters for the repo:** Acts as a reality-check before attempting low-latency experiments.
- **Exercise:** Document the key engineering and measurement requirements you would need to run a sub-second experiment; identify gaps in the current repo.
