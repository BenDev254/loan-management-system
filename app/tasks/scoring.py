from celery import Celery
import requests
import time

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

SCORING_ENGINE_URL = "https://scoringtest.credable.io/api/v1"

@celery_app.task(bind=True, max_retries=3)
def fetch_score(self, token: str):
    """Retries fetching the credit score with a delay."""
    url = f"{SCORING_ENGINE_URL}/score/retrieve"
    payload = {"token": token}
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as exc:
        raise self.retry(exc=exc, countdown=10)  # Retry every 10s (max 3 attempts)
