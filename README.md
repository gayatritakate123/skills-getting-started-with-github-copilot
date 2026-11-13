# Mergington High School API

A small FastAPI application for viewing extracurricular activities, signing up students, and looking up cities by country or region.

## Getting Started

Requirements: Python 3.10 or newer.

1. Create and activate a virtual environment:

	```sh
	python -m venv .venv
	source .venv/bin/activate
	```

	On Windows PowerShell, activate it with `.venv\Scripts\Activate.ps1`.

2. Install the project dependencies:

	```sh
	pip install -r requirements.txt
	```

3. Start the development server from the repository root:

	```sh
	uvicorn src.app:app --reload
	```

4. Open [http://localhost:8000](http://localhost:8000) for the application. Interactive API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/activities` | List extracurricular activities and participants. |
| `POST` | `/activities/{activity_name}/signup?email=student@example.com` | Sign up a student for an activity. |
| `GET` | `/countries/{country}/cities` | List cities in a country. |
| `GET` | `/countries/{country}/cities?region={region}` | List cities in a region or state within a country. |

The cities route uses the public CountriesNow API, so it requires an internet connection. For example, `GET /countries/Spain/cities` returns the cities reported for Spain. A regional lookup can be made with `GET /countries/Spain/cities?region=Madrid`.

## Tests

Run the test suite from the repository root:

```sh
pytest
```

The city-route tests mock the external data service, so they do not need an internet connection.

## GitHub Copilot Exercise

[Open the exercise](https://github.com/gayatritakate123/skills-getting-started-with-github-copilot/issues/1).

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

