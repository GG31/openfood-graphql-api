from unittest.mock import MagicMock
from ..core import Object

from .products import Products
import config

test_config = config.get_config('test')


def test_get_product_empty():
    db = MagicMock()
    db.find.return_value = []
    products = Products(test_config, MagicMock(), { 'test': db })
    result = products.get_products(first=10, after=0)
    db.find.assert_called_once_with({}, skip=0, limit=10)
    assert len(result.products) == 0
    assert result.total == 0


def test_get_product_with_result():
    db = MagicMock()
    data = { 'product_name': 'test', 'ingredients': [{ 'id': 'id_test', 'text': 'test' }] }
    db.find.return_value = [data]
    products = Products(test_config, MagicMock(), { 'test': db })
    result = products.get_products(first=10, after=0)
    db.find.assert_called_once_with({}, skip=0, limit=10)
    assert len(result.products) == 1
    assert result.products[0] == Object(name='test', ingredients=[Object(id='id_test', name='test')])
    assert result.total == 1
