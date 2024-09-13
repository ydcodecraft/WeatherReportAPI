from unittest.mock import MagicMock
from sqlalchemy.orm import Session

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import City, AccessHistory
from enums import RequestStatus
from crud import get_city_by_id, create_api_access_history, get_recent_successful_api_access_history
from schemas import accessHistorySchemas


def test_get_city_by_id():
    # Mock the db session and city instance
    db = MagicMock(spec=Session)
    mock_city = MagicMock(spec=City)
    mock_city.id = 1
    mock_city.name="Dortmund"
    db.query().filter().first.return_value = mock_city
    
    result = get_city_by_id(db, 1)
    db.query().filter().first.assert_called_once()
    assert result.id == 1
    assert result.name == "Dortmund"

def test_create_api_access_history():
    # Mock the db session and access history instance
    db = MagicMock(spec=Session)
    mock_access_history = MagicMock(spec=AccessHistory)
    
    # Define a mock schema input
    mock_schema = accessHistorySchemas.AccessHistoryCreate(city_id=1, status=RequestStatus.Success)
    
    # Call the function
    result = create_api_access_history(db, mock_schema)
    
    # Assert that db.add, db.commit, and db.refresh are called
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()
    
    assert result.city_id == 1
    assert result.status == RequestStatus.Success


def test_get_recent_successful_api_access_history():
    # Mock the db session and access history instance
    db = MagicMock(spec=Session)
    mock_access_history = [MagicMock(spec=AccessHistory) for _ in range(5)]
    db.query().filter().order_by().limit().all.return_value = mock_access_history
    
    # Call the function
    result = get_recent_successful_api_access_history(db, limit=5)
    
    # Assert the result is correct
    assert len(result) == 5
    assert result == mock_access_history