import json
import time



def python_cost_calculate(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    # Variable definitions:
    # price per request, free tier limit requests, free tier compute limit,
    # lambda cost per GBs

    request_price = 0.0000002

    free_tier_request = 1000000

    free_tier_compute = 400000


    lambda_gbs_cost = 0.00001667

    # Retreive variables from HHTP request

    memory_allocation = int (data['memory_allocation'])
    execution_times   = int (data['execution_times'])
    execution_length  = float (data['execution_length'])
    free_tier_check   = str (data['free_tier_check'])


    # Total compute (seconds)
    # Total compute (GB-s)

    total_request_charges_free = (execution_times - free_tier_request) * request_price
    total_request_charges_paid = execution_times * request_price


    total_compute_seconds = execution_times * execution_length
    total_compute_gbs = total_compute_seconds * (memory_allocation / float(1024))
    monthly_billable_compute = total_compute_gbs - free_tier_compute

    monthly_compute_charges_free = (monthly_billable_compute * lambda_gbs_cost) + total_request_charges_free
    monthly_compute_charges_paid = (total_compute_gbs * lambda_gbs_cost) + total_request_charges_paid

    if (free_tier_check == 'true'):
        monthly_compute_charges_final = monthly_compute_charges_free
    else:
        monthly_compute_charges_final = monthly_compute_charges_paid


    # JSON Response
    results = {
        'monthly_cost': monthly_compute_charges_final,
        'timestamp': timestamp,
        'check': free_tier_check
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