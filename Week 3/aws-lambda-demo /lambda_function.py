# Runtime settings
# Runtime: Python 3.6
# Handler: lambda_function.lambda_handler
def lambda_handler(event, context):
    message = 'Hello {}'.format(event["queryStringParameters"]["name"])
    return { 'body': message }