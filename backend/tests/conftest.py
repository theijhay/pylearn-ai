import warnings
import pytest

# Ignore specific warnings from SQLAlchemy 2.0
warnings.filterwarnings("ignore", category=DeprecationWarning)

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    # Ensure the database is set up before running tests
    from backend.models import Base, engine
    Base.metadata.create_all(bind=engine)
