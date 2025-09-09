# Change Tracker Dashboard

## Overview
The Change Tracker Dashboard is a Streamlit web application for collecting questionnaire responses and visualizing change-related metrics. It uses DuckDB as a lightweight embedded database to store users, questions, and answers. The app maps user responses to numeric scores and renders interactive visualizations to help teams assess business performance and benefits realization.

## Repository structure
- [`app.py`](app.py:1) — application entry point and navigation.
- [`pages.py`](pages.py:1) — Streamlit pages: login, questions, and results.
- [`app_result.py`](app_result.py:1) — result page rendering helpers and alternate visualizations.
- [`database_client.py`](database_client.py:1) — DuckDB connection and database helper functions.
- [`modules.py`](modules.py:1) — plotting and utility functions (figure generation, helpers).
- [`map_answers_to_scores.json`](map_answers_to_scores.json:1) — mapping of answer choices to numeric scores used for scoring.
- [`change_tracker.db`](change_tracker.db:1) — example DuckDB database included for convenience.
- `DDL/` — SQL files for creating the database schema (see [`DDL/create_questions.sql`](DDL/create_questions.sql:1), etc.).
- `DML/` — example queries and data operations (see [`DML/answers_query.sql`](DML/answers_query.sql:1)).
- `just_testing/` — notebooks and scripts used for development experiments.
- [`requirements.txt`](requirements.txt:1)
- [`.streamlit/config.toml`](.streamlit/config.toml:1)

## Features
- Secure email-based login backed by DuckDB.
- Dynamic questionnaire loaded from the database.
- Answer-to-score mapping using [`map_answers_to_scores.json`](map_answers_to_scores.json:1).
- Immediate persistence of submissions into the DuckDB file.
- Interactive visualizations using Plotly / Matplotlib via helpers in [`modules.py`](modules.py:1).

## Getting started
Prerequisites:
- Python 3.9+
- pip

1. Clone the repository
   git clone <repository-url>

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

The main Streamlit navigation is handled in [`app.py`](app.py:1) which imports page definitions from [`pages.py`](pages.py:1).

## How it works (high level)
1. User opens the app and logs in with an email (login flow implemented in [`pages.py` — show_login_page](pages.py:17)).
2. Questions are loaded from the database and rendered on the questions page (see [`pages.py` — show_questions](pages.py:48)).
3. User answers are mapped to numeric scores using [`map_answers_to_scores.json`](map_answers_to_scores.json:1). Scoring and JSON handling are implemented across [`pages.py`](pages.py:48) and [`database_client.py`](database_client.py:1).
4. Submissions are saved to the DuckDB file (`change_tracker.db`) and the results page computes aggregates and renders charts using functions in [`modules.py`](modules.py:1) and [`app_result.py`](app_result.py:1).

## Database
- The project uses DuckDB for a lightweight embedded analytical database. Schema creation SQL files live in the `DDL/` folder:
  - [`DDL/create_users.sql`](DDL/create_users.sql:1)
  - [`DDL/create_questions.sql`](DDL/create_questions.sql:1)
  - [`DDL/create_drivers.sql`](DDL/create_drivers.sql:1)
  - [`DDL/create_answers.sql`](DDL/create_answers.sql:1)
- Example queries: [`DML/answers_query.sql`](DML/answers_query.sql:1)
- To rebuild the DB from scratch, run the SQL files in `DDL/` against a new DuckDB file and optionally seed with example data.

## Configuration
- Streamlit configuration: [`.streamlit/config.toml`](.streamlit/config.toml:1)
- Scoring map: [`map_answers_to_scores.json`](map_answers_to_scores.json:1)
- To use a different DuckDB file, update the connection settings in [`database_client.py`](database_client.py:1).

## Development notes
- Plot helpers are in [`modules.py`](modules.py:1). Notable functions:
  - `figure_scale_by_value` — builds plot scaled by absolute values.
  - `figure_scale_by_percentage` — builds plot scaled as percentages.
- Page rendering is split between [`pages.py`](pages.py:1) (main application flow) and [`app_result.py`](app_result.py:1) (alternate result visualizations).
- Experimentation and quick tests are in the `just_testing/` folder (notebooks and small scripts).

## Adding questions or updating scoring
- Add or update questions via the DDL SQL scripts or by inserting rows directly into the database.
- Update the answer-to-score mapping in [`map_answers_to_scores.json`](map_answers_to_scores.json:1) to change how responses are converted to numeric scores.

## Troubleshooting
- If Streamlit fails to start, verify dependencies are installed and Python is compatible.
- If there are DB errors, check file permissions on `change_tracker.db` and review the contents of the SQL files in `DDL/`.
- For visualization issues, inspect functions in [`modules.py`](modules.py:1) and how they're called from [`pages.py`](pages.py:1) / [`app_result.py`](app_result.py:1).

## License
This project is licensed under the MIT License — see the included [`LICENSE`](LICENSE:1) file.

## Contributors
- Primary author: Your Name
- See git history for additional contributors.

## Contact
Open issues in the GitHub repository to report bugs or request features.