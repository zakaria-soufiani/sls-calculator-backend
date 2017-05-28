import json
import time



def python_cost_calculate(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    request_price = 0.0000002

    free_tier_request = 1000000

    free_tier_compute = 400000

    lambda_gbs_cost = 0.00001667

    memory_allocation = int (data['memory_allocation'])
    execution_times   = int (data['execution_times'])
    execution_length  = float (data['execution_length'])

    # Total compute (seconds)
    # Total compute (GB-s)

    total_request_charges = (execution_times - free_tier_request) * request_price

    total_compute_seconds   = execution_times * execution_length

    total_compute_gbs = total_compute_seconds * (memory_allocation / float(1024))

    monthly_billable_compute = total_compute_gbs - free_tier_compute

    monthly_compute_charges = (monthly_billable_compute * lambda_gbs_cost) + total_request_charges

    monthly_compute_charges_string = "$"+str(monthly_compute_charges)

    results = {
        'monthly_cost': monthly_compute_charges_string,
        'timestamp': timestamp
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