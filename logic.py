import json



def calculate(event, context):
    data = json.loads(event['body'])

    num1 = int(data['num1'])
    num2 = int(data['num2'])

    addition = num1 + num2
    multiplication = num1 * num2

    results = {
        'addition': addition,
        'multiplication': multiplication
    }
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(results),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true"
        }
    }

    return response