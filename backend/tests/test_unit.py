import pytest
from backend.models import session, UserProgress
import logging
import os
from app import app, logger
from app import app, file_handler
import pytest
from models import UserProgress, session

def test_create_user_progress():
    # Arrange
    new_progress = UserProgress(user_id=1, progress_info="50%")
    
    # Act
    session.add(new_progress)
    session.commit()
    
    # Assert
    saved_progress = session.query(UserProgress).filter_by(user_id=1).first()
    assert saved_progress is not None
    assert saved_progress.progress_info == "50%"

def test_logging():
    log_file = 'logs/app.log'

    # Clear the log file before the test
    if os.path.exists(log_file):
        os.remove(log_file)

    # Log a test message
    logger = logging.getLogger('test')
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    logger.info('Test log message')

    # Read the log file
    with open(log_file, 'r') as f:
        logs = f.read()

    assert 'Test log message' in logs
