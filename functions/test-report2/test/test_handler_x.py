from handler_x import lambda_handler


def test_lambda_handler():
    assert 'ok' == lambda_handler('', None)
