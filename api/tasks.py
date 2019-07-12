from djanog_celery_setup.celery import app
from structlog import get_logger


@app.task(bind=True)
def debug_task(self, now):
    logger = get_logger(__name__)
    logger.info("executing_task", now=now, retry=self.retry)
    return