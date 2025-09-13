# SIH Mentor/Admin Dashboard Backend

This project contains the FastAPI backend for the SIH Mentor and Admin Dashboard. It includes a secure authentication system using JWT, a PostgreSQL database connection, and API endpoints to retrieve role-specific dashboard data.

## Project Setup

### Prerequisites

- Python 3.9+
- PostgreSQL server running

### 1. Setup Environment

Create and activate a Python virtual environment in the `sih_backend` directory.

'''bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
