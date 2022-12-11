from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web__app


class APITestCase(TestCase):

  def setUP(self):
    self.client = TestClient()
