# TP04: Containerization and Big Data Environment Deployment Using Docker

Big Data Analytics, Master 2 IA & Data Science, University of Eloued

## Project
A Python script analyses the CMS Open Payments dataset (Jan to Mar 2025, 3,866,795 rows) and prints the total amount, the top 5 states and the top 5 companies. It is packaged in Docker and run with containers and Docker Compose.

## Files
- `analysis.py`: reads the CSV in chunks and prints the results
- `make_dataset.py`: builds `data/dataset.csv` from the original CMS file (same cleaning as TP03)
- `Dockerfile`, `compose.yaml`, `requirements.txt`
- `screenshots/`: proof for each task
- `report/`: the lab report

## Dataset
The CSV is too large for GitHub, so it is not included. Download the CMS Open Payments 2025 general payments file, then run `python make_dataset.py` to create `data/dataset.csv`.

## Run it
```
docker pull beyheyam/tp04-analysis:v1
docker run --rm -v ./data:/app/data:ro beyheyam/tp04-analysis:v1
```
Or with Compose:
```
docker compose up --build
docker compose down
```

## Docker Hub
https://hub.docker.com/r/beyheyam/tp04-analysis

## Screenshots
| Task | Files |
|---|---|
| 1. Installation | `task1-docker-version.png`, `task1-hello-world.png` |
| 2. Image | `task2-build.png`, `task2-run-test.png`, `task2-push.png`, `task2-dockerhub.png`, `task2-pull.png` |
| 3. Containers | `task3-ps.png`, `task3-network.png`, `task3-logs.png`, `task3-docker-desktop.png` |
| 4. Compose | `task4-up.png`, `task4-ps.png`, `task4-down.png` |

All files are in the `screenshots/` folder. The answers to the questions are in the report.