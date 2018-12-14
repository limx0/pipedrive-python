import os

import pytest

from pipedrive.client import Client


@pytest.fixture()
def client():
    c = Client(api_base_url=os.environ['PIPEDRIVE_BASE_URL'])
    c.set_token(os.environ['PIPEDRIVE_API_KEY'])
    return c


def test_deal_fields(client):
    resp = client.get_deal_fields(limit=500)['data']
    assert resp
