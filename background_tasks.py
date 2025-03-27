from celery import shared_task
import time
import requests
from config import SCORING_API_TOKEN

@shared_task(bind=True, max_retries=3, default_retry_delay=5)  # Retry 3 times with 5s delay
def retry_scoring(self, customer_number):
    try:
        response = requests.get(
            f"https://scoringtest.credable.io/api/v1/scoring/initiateQueryScore/{customer_number}",
            headers={"client-token": SCORING_API_TOKEN}
        )
        response.raise_for_status()
        token = response.json().get("token")

        # Wait for processing (retry logic)
        for _ in range(3):  # 3 retries
            time.sleep(5)
            score_response = requests.get(
                f"https://scoringtest.credable.io/api/v1/scoring/queryScore/{token}",
                headers={"client-token": SCORING_API_TOKEN}
            )
            if score_response.status_code == 200:
                return score_response.json()
        
        return {"status": "FAILED", "message": "Scoring engine did not respond"}

    except Exception as e:
        self.retry(exc=e)
