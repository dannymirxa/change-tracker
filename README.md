# Change Tracker Dashboard

## Description

The Change Tracker Dashboard is a web application built with Streamlit that allows users to interact with a set of questions and visualize results based on their inputs. The application is connected to a DuckDB database and provides a login interface for users.

## Features

- **Login Interface**: Secure login mechanism using user emails stored in DuckDB.
- **Dynamic Questionnaire**: Questions are loaded from the database, allowing for easy updates.
- **Real-time Scoring**: User answers are scored and stored in the database.
- **Visualization**: Displays user data in a dashboard using charts to present 'Leadership Effectiveness'.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **DuckDB**: A lightweight database used to store and query user and questionnaire data.
- **Pandas**: Data manipulation and analysis library.
- **Matplotlib**: Visualization library for plotting user scores.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd change-tracker
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage Instructions

- **Login** with your email to access the dashboard.
- **Interact** with the questionnaire and submit your answers to view the results.
- **Navigate** through the application to explore different sections including the Welcome page and Results Dashboard.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Your Name