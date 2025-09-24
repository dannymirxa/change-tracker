# Change Tracker Dashboard

## Overview
The Change Tracker Dashboard is a Streamlit-based web application for collecting questionnaire responses and visualizing change-related metrics. It uses DuckDB as a lightweight embedded database to store users, questions, and answers. The app maps user responses to numeric scores (via a configurable JSON map) and renders interactive visualizations to help teams assess business performance and benefits realization.

## Quick links (important files)
- [`app_dashboard.py`](app_dashboard.py:1) — main dashboard entry point (summary / results view).
- [`app_survey.py`](app_survey.py:1) — survey / questionnaire entry point.
- [`app_result.py`](app_result.py:1) — helpers and alternate result visualizations.
- [`database_client.py`](database_client.py:1) — DuckDB connection and database helper functions.
- [`modules.py`](modules.py:1) — plotting and utility functions (figure generation, helpers).
- [`map_answers_to_scores.json`](map_answers_to_scores.json:1) — mapping of answer choices to numeric scores used for scoring.
- [`change_tracker.db`](change_tracker.db:1) — example DuckDB file included for convenience.
- `pages/` — modular Streamlit pages:
  - [`pages/login.py`](pages/login.py:1)
  - [`pages/questions.py`](pages/questions.py:1)
  - [`pages/result_latest.py`](pages/result_latest.py:1)
  - [`pages/result_timeline.py`](pages/result_timeline.py:1)
  - [`pages/welcome.py`](pages/welcome.py:1)
- `schema/` — CSV and SQL used to create / seed the database (see [`schema/schema.sql`](schema/schema.sql:1)).
- `just_testing/` — development notebooks and scripts for experiments.

## Features
- Email-based login flow persisted in DuckDB.
- Dynamic questionnaire loaded from the DB and rendered in Streamlit pages.
- Answer-to-score mapping via [`map_answers_to_scores.json`](map_answers_to_scores.json:1).
- Submissions are saved to a DuckDB file (`change_tracker.db`) for analysis.
- Interactive visualizations built with Plotly/Matplotlib helpers in [`modules.py`](modules.py:1).

## Repository structure (high level)
- Top-level application entrypoints:
  - [`app_dashboard.py`](app_dashboard.py:1)
  - [`app_survey.py`](app_survey.py:1)
- Application helpers and visuals:
  - [`app_result.py`](app_result.py:1)
  - [`modules.py`](modules.py:1)
- Database & configuration:
  - [`database_client.py`](database_client.py:1)
  - [`map_answers_to_scores.json`](map_answers_to_scores.json:1)
  - [`change_tracker.db`](change_tracker.db:1)
- Streamlit pages under `pages/` (see section above).
- Auxiliary: `schema/`, `just_testing/`, `.streamlit/config.toml`, and example HTML outputs.

## Getting started

Prerequisites:
- Python 3.9+ recommended
- pip

1. Clone the repository
   git clone <repository-url>

2. Create a virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate   # on Linux / macOS
   .venv\Scripts\activate      # on Windows (PowerShell/cmd differences)

3. Install dependencies
   pip install -r requirements.txt

4. Run the app (pick the entrypoint you want)
   - To run the survey UI:
     streamlit run app_survey.py
   - To run the results/dashboard UI:
     streamlit run app_dashboard.py

Note: The repository contains multiple Streamlit pages and entrypoints. Pick the appropriate entrypoint based on whether you want to submit responses or view aggregated results.

## How it works (high-level flow)
1. A user opens the app and signs in using an email (login flow implemented in [`pages/login.py`](pages/login.py:1)).
2. The survey questions are loaded from the DuckDB database and rendered by the survey page (see [`pages/questions.py`](pages/questions.py:1)).
3. User answers are mapped to numeric scores using [`map_answers_to_scores.json`](map_answers_to_scores.json:1). Scoring logic lives across [`pages/questions.py`](pages/questions.py:1) and [`database_client.py`](database_client.py:1).
4. Submissions are persisted into the DuckDB file (`change_tracker.db`) and the results/dashboard pages compute aggregates and render charts using functions from [`modules.py`](modules.py:1) and [`app_result.py`](app_result.py:1).

## Database
- This project uses DuckDB as an embedded analytical database. The included example DB file is [`change_tracker.db`](change_tracker.db:1).
- Use the SQL in `schema/` to recreate or seed the database:
  - [`schema/schema.sql`](schema/schema.sql:1)
  - CSVs in [`schema/`](schema/:1) (questions, users, surveys, drivers, answers)
- To rebuild the DB from scratch: create a new DuckDB file and run the SQL in `schema/schema.sql`, then optionally load CSVs.

## Configuration
- Streamlit configuration: `.streamlit/config.toml` (project Streamlit settings).
- Scoring map: [`map_answers_to_scores.json`](map_answers_to_scores.json:1) — modify this to change how textual answers map to numeric scores.
- Database connection: update [`database_client.py`](database_client.py:1) to point to a different DuckDB file if required.

## Development notes
- Plot/visual helpers are in [`modules.py`](modules.py:1). Two commonly used helpers:
  - `figure_scale_by_value` — build plots scaled by absolute values (see [`modules.py`](modules.py:1) for signature).
  - `figure_scale_by_percentage` — build plots scaled as percentages.
- Result rendering is split between page code in `pages/` and helpers in [`app_result.py`](app_result.py:1).
- The `just_testing/` folder contains quick experiments and notebooks used during development (not required for production).

## Adding questions or updating scoring
- Add or update questions by inserting rows in the database (use DuckDB or run the SQL scripts / CSV imports in `schema/`).
- Update score mapping by editing [`map_answers_to_scores.json`](map_answers_to_scores.json:1). The application will convert stored text answers to numeric values according to this map when computing aggregates.

## Troubleshooting
- Streamlit won't start: confirm Python version and that dependencies are installed (see `requirements.txt`).
- Database errors: check file permissions on [`change_tracker.db`](change_tracker.db:1) and ensure the schema matches expected columns (see `schema/schema.sql`).
- Visualization problems: inspect plotting helpers in [`modules.py`](modules.py:1) and see how they're used in `pages/` and [`app_result.py`](app_result.py:1).

## Tests & experiments
- Quick tests and data imports live under `just_testing/`. Files of interest:
  - `just_testing/test_duckdb.py`
  - `just_testing/test_scoring.py`
  - `just_testing/test_streamlit.py`

## License
This project is licensed under the MIT License — see the included [`LICENSE`](LICENSE:1) file (if present).

## Contributors
- Primary author: Your Name
- See git history for additional contributors.

## Contact
Open issues in the GitHub repository to report bugs or request features.