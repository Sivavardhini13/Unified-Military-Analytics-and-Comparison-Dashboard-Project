# Unified Military Analytics and Comparison Dashboard 

## Project Overview
A comprehensive interactive dashboard suite for analyzing global military power in 2025, featuring data from 140+ countries with 50+ defense and economic indicators. The project provides cross-platform flexibility with deployments in Tableau, Power BI, Streamlit, and Dash.

## Key Features
- **Quick Stats**: Global overview of rankings, trends, and highlights
- **Nation Overview**: Detailed analysis of individual country capabilities
- **Compare Powers**: Side-by-side military and economic comparison
- **Coalition Builder**: Interactive simulation of alliance strength and combined assets

## Project Structure - Milestone & Module Organized

```
Unified-Military-Analytics-and-Comparison-Dashboard-DV-1/
│
├── MILESTONE 1: DATA COLLECTION & PREPARATION (Weeks 1-2)
│   │
│   ├── milestone_1_data_collection/
│   │   │
│   │   ├── MODULE 1: Scraping Setup & Execution
│   │   │   └── module_1_scraping/
│   │   │       ├── scrape_military_metrics.py      # Main scraping script
│   │   │       ├── scraper_config.json             # URLs and settings
│   │   │       ├── html_cache/                     # Per-country HTML (debug)
│   │   │       └── logs/
│   │   │
│   │   └── MODULE 2: Data Cleaning & Structuring
│   │       └── module_2_cleaning/
│   │           ├── clean_data.py                   # Cleaning pipeline
│   │           ├── data_mapping.json               # Column standardization
│   │           ├── validation_rules.json           # Data quality checks
│   │           └── notebooks/
│   │               └── 02_data_cleaning.ipynb      # Cleaning workflow
│   │
│   └── Data Storage (Module 1 & 2 outputs)
│       ├── data/raw/
│       │   ├── military_raw_data.csv               # Raw scraped (140+ countries)
│       │   ├── links_for_military_data.txt         # URL list
│       │   └── scraping_report.md                  # Scraping summary
│       └── data/processed/
│           ├── military_cleaned.csv                # Cleaned dataset
│           ├── data_quality_report.md              # Cleaning summary
│           └── quality_metrics.json                # Validation results
│
├── MILESTONE 2: KPI ENGINEERING & TABLEAU PREP (Weeks 3-4)
│   │
│   ├── milestone_2_kpi_engineering/
│   │   │
│   │   ├── MODULE 3: KPI Feature Engineering
│   │   │   └── module_3_kpi_feature_engineering/
│   │   │       ├── generate_kpis.py                # KPI calculation engine
│   │   │       ├── kpi_definitions.json            # KPI formulas
│   │   │       ├── metadata_enrichment.py          # Region/Alliance data
│   │   │       └── notebooks/
│   │   │           └── 03_kpi_engineering.ipynb    # KPI validation
│   │   │
│   │   └── MODULE 4: Dashboard Planning & Prototyping
│   │       └── module_4_dashboard_planning/
│   │           ├── wireframes/                     # Dashboard sketches
│   │           ├── interaction_design.md           # UI/UX documentation
│   │           ├── filter_specifications.json      # Filter definitions
│   │           └── prototype_dashboard.twbx        # Tableau prototype
│   │
│   └── Data Storage (Module 3 output)
│       └── data/kpi/
│           ├── military_final.xlsx                 # Wide format (all KPIs)
│           ├── military_final_long.csv             # Long format (Tableau)
│           └── kpi_validation_report.md            # KPI accuracy check
│
├── MILESTONE 3: FULL DASHBOARD DEVELOPMENT (Weeks 5-6)
│   │
│   ├── milestone_3_dashboard_development/
│   │   │
│   │   ├── MODULE 5: Quick Stats & Nation Overview
│   │   │   └── module_5_quick_stats_nation_overview/
│   │   │       ├── quick_stats_dev.twbx            # Quick Stats workbook
│   │   │       ├── nation_overview_dev.twbx        # Nation Overview workbook
│   │   │       ├── quick_stats_spec.md             # Feature specifications
│   │   │       └── nation_overview_spec.md         # Feature specifications
│   │   │
│   │   ├── MODULE 6: Compare Powers & Coalition Builder
│   │   │   └── module_6_compare_coalition/
│   │   │       ├── compare_powers_dev.twbx         # Compare Powers workbook
│   │   │       ├── coalition_builder_dev.twbx      # Coalition Builder workbook
│   │   │       ├── compare_spec.md                 # Feature specifications
│   │   │       └── coalition_spec.md               # Feature specifications
│   │   │
│   │   └── Integration/
│   │       ├── global_military_firepower_2025.twbx # FINAL INTEGRATED WORKBOOK
│   │       ├── integration_notes.md                # Integration details
│   │       └── parameter_definitions.json          # Tableau parameters
│   │
│   └── Dashboard Variants (Alternative platforms)
│       ├── dashboards/power_bi/
│       │   ├── Global_Military_Powers_Stats.pbix   # Power BI version
│       │   └── powerbi_config.json
│       ├── dashboards/streamlit/
│       │   ├── app.py
│       │   ├── pages/
│       │   │   ├── 01_quick_stats.py
│       │   │   ├── 02_nation_overview.py
│       │   │   ├── 03_compare_powers.py
│       │   │   └── 04_coalition_builder.py
│       │   └── requirements.txt
│       └── dashboards/dash/
│           ├── app.py
│           ├── callbacks.py
│           ├── layouts.py
│           └── requirements.txt
│
├── MILESTONE 4: FINAL REVIEW & DELIVERY (Weeks 7-8)
│   │
│   ├── milestone_4_final_delivery/
│   │   │
│   │   ├── MODULE 7: Testing & Debugging
│   │   │   └── module_7_testing/
│   │   │       ├── qa_checklist.md                 # QA testing document
│   │   │       ├── test_results.md                 # Test execution results
│   │   │       ├── known_issues.md                 # Bug tracking
│   │   │       └── tests/
│   │   │           ├── test_scraping.py
│   │   │           ├── test_data_quality.py
│   │   │           └── test_kpi_calculations.py
│   │   │
│   │   └── MODULE 8: Documentation & GitHub Release
│   │       └── module_8_documentation/
│   │           ├── FINAL_README.md                 # Comprehensive README
│   │           ├── SCRAPING_GUIDE.md               # How to scrape
│   │           ├── DASHBOARD_USER_GUIDE.md         # Dashboard usage
│   │           ├── KPI_DEFINITIONS.md              # KPI explanations
│   │           ├── DATA_DICTIONARY.md              # Data field reference
│   │           ├── ARCHITECTURE.md                 # System design
│   │           └── INSTALLATION_GUIDE.md           # Setup instructions
│   │
│   └── Release Artifacts/
│       ├── CHANGELOG.md
│       ├── requirements.txt                        # Python dependencies
│       └── .gitignore
│
├── Supporting Directories
│   ├── configs/                                    # Configuration files (all)
│   ├── scripts/                                    # Utility scripts
│   └── tests/                                      # Test suite
│
└── Documentation (Cross-Milestone)
    ├── docs/
    │   ├── PROJECT_STATEMENT.md                   # Project overview
    │   ├── MILESTONES.md                          # Timeline & deliverables
    │   └── PROGRESS_TRACKER.md                    # Status updates
    └── README.md                                  # This file

```

## Milestones & Timeline

### Milestone 1: Data Collection and Preparation (Weeks 1–2)
- **Module 1**: Scraping Setup and Execution
  - Output: `scrape_military_metrics.py`, `data/raw/military_raw_data.csv`
- **Module 2**: Data Cleaning and Structuring
  - Output: `data/processed/military_cleaned.csv`, `notebooks/02_data_cleaning.ipynb`

### Milestone 2: KPI Engineering and Tableau Prep (Weeks 3–4)
- **Module 3**: KPI Feature Engineering
  - Output: `data/kpi/military_final.xlsx`, `scripts/generate_kpis.py`
- **Module 4**: Dashboard Planning and Prototyping
  - Output: Dashboard storyboard, prototype application

### Milestone 3: Full Dashboard Development (Weeks 5–6)
- **Module 5**: Build Quick Stats and Nation Overview
  - Output: Quick Stats and Nation Overview dashboards
- **Module 6**: Build Compare Powers and Coalition Builder
  - Output: All 4 dashboards fully integrated

### Milestone 4: Final Review and Delivery (Weeks 7–8)
- **Module 7**: Testing and Debugging
  - Output: QA checklist, debugged workbook
- **Module 8**: Documentation and GitHub Release
  - Output: GitHub repository, final documentation

## Key Files Location

| File | Location | Purpose |
|------|----------|---------|
| Raw Data | `data/raw/military_raw_data.csv` | Original scraped data from GlobalFirepower.com |
| Cleaned Data | `data/processed/military_cleaned.csv` | Data after cleaning and standardization |
| Final KPI Dataset | `data/kpi/military_final.xlsx` | Complete dataset with all KPIs |
| Tableau Dashboard | `dashboards/tableau/global_military_firepower_2025.twbx` | Primary Tableau workbook |
| Power BI Dashboard | `dashboards/power_bi/Global_Military_Powers_Stats.pbix` | Power BI alternative |
| Configuration Files | `configs/` | All system configurations |

## KPI Definitions

The following KPIs are calculated in `generate_kpis.py`:

1. **Power Index Rank Gap**: Ranking difference between consecutive countries
2. **Assets per Capita**: Military assets divided by population
3. **Budget-to-GDP Ratio**: Defense budget as percentage of GDP
4. **Personnel per 1000**: Active military personnel per 1000 population
5. **Equipment Density**: Total equipment count per land area

## Getting Started

### Prerequisites
- Python 3.8+
- Tableau Public/Desktop (for Tableau dashboards)
- Power BI Desktop (for Power BI dashboards)
- Required packages: see `requirements.txt`

### Setup Instructions
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Place `links_for_military_data.txt` in `data/raw/`
4. Run scraping: `python scripts/scrape_military_metrics.py`
5. Run cleaning: `python scripts/clean_data.py`
6. Generate KPIs: `python scripts/generate_kpis.py`
7. Open dashboards in Tableau or Power BI

## Data Sources
- **Primary**: GlobalFirepower.com (scraped)
- **File**: `data/raw/links_for_military_data.txt` (140+ country URLs)

## Dashboard Modules

### Quick Stats
- Top 10 countries by Power Index
- Regional distribution
- Alliance breakdowns
- Trend indicators

### Nation Overview
- Country profile with all metrics
- Bar and radar charts
- Rank comparisons
- Historical trends

### Compare Powers
- Side-by-side country comparison
- Key metrics highlighted
- Percentage difference calculations
- Custom metric selection

### Coalition Builder
- Multi-country selection
- Aggregated coalition metrics
- Strength comparisons
- What-if scenarios

## Contributors
- Project Lead: [Your Name]
- Data Engineering: [Team]
- Dashboard Development: [Team]

## License
[Specify License - MIT, GPL, etc.]

## Support & Documentation
- For issues: Check `docs/` folder
- For questions: See `DASHBOARD_GUIDE.md`
- For data: See `DATA_DICTIONARY.md`

## Last Updated
February 2026

---

**Status**: Project Structure Initialized | Next: Data Collection Phase

