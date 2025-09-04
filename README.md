# Change Tracker Dashboard

## Description
The Change Tracker Dashboard is a web application built with Streamlit that allows users to interact with a questionnaire and visualize results based on their inputs. The application interfaces with a DuckDB database, providing a secure login interface and dynamic feature set for user interaction.

## Features

- **Login Interface**: Secure login using user emails stored in DuckDB. Users are greeted by name upon login.
- **Dynamic Questionnaire**: Questions are loaded from the database and users' responses are mapped and scored based on predefined mappings.
- **Real-time Scoring and Submission**: Scores are calculated as users respond and results are saved into the database immediately upon submission.
- **Interactive Results Visualization**: Utilize Plotly to display average scores of business drivers in an expandable and interactive format, providing insights into 'Business Performance' and 'Benefits Realization'.

## Technologies Used

- **Streamlit**: For building the interactive web UI.
- **DuckDB**: A lightweight database for storing user and questionnaire data.
- **Pandas**: For data manipulation and conversion of JSON responses.
- **Matplotlib and Plotly**: Visualization libraries for generating detailed dashboards and insights.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd change-tracker
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage Instructions

- **Login** with your email to access and explore the dashboard.
- **Answer** questions related to business performance and realization.
- **Submit** your responses to store data and view results.
- **Navigate** through interactive dashboard sections like Business Performance and Benefits Realization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

## Authors

- Your Name