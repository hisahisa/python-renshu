

def test_lambda_handler():
    from handler_test import lambda_handler
    assert 'ok' == lambda_handler('', None)
