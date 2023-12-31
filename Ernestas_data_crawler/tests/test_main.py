
from requests import patch
from Ernestas_data_crawler import extract_data_from_article
from definitions import test_dir
import pytest
from unittest.mock import Mock
from unittest.mock import patch
from requests import Response


@pytest.fixture
def article():
    with open(test_dir / "article.html") as f:
        content = f.read()
    return content
        


def fake_get(url: str) -> str:
    default_response = Response()
    default_response.status_code = 200
    content = "<html></html>"
    if url == "https://www.lrytas.lt/search?q=vakcinavimas":
        with open (test_dir / "article.html") as f:
            content = f.read()
    default_response.text = content
    return default_response
    


def test_process_page():
    with patch("requests.get", wraps = fake_get) as wrapped_get:
        main()
        
        