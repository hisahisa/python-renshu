import pandas as pd
from utils.layer.util.mysql import Mysql


def lambda_handler(event, context):
    # TODO implement

    # my = Mysql()
    # print(1)
    # select_sql = 'select * from testdb.USER;'
    # print(2)
    # df = pd.read_sql(my.text(select_sql), my.engine)

    print(event)
    return 0

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
