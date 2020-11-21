## Exercise 3.1 Creating an AWS Lambda Function

![week3-ex-3-1-1](week3-ex-3-1-1.png)

![week3-ex-3-1-2](week3-ex-3-1-2.png)

![week3-ex-3-1-3](week3-ex-3-1-3.png)

```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": [
                    "arn:aws:logs:*:*:*"
                ]
            }
        ]
    }
```

![week3-ex-3-1-4](week3-ex-3-1-4.png)

```python
def lambda_handler(event, context):
    city_str = event['city_str']
    response = {
        "city_str": city_str,
        "temp_int": 74
    }
    return response
```

![week3-ex-3-1-5](week3-ex-3-1-5.png)

![week3-ex-3-1-6](week3-ex-3-1-6.png)

```json
    {
     "city_str": "LA"
    }
```

![week3-ex-3-1-7](week3-ex-3-1-7.png)

![week3-ex-3-1-8](week3-ex-3-1-8.png)

![week3-ex-3-1-9](week3-ex-3-1-9.png)

![week3-ex-3-1-10](week3-ex-3-1-10.png)

```json
    {
       "city_str": "SEATTLE"
    }
```

![week3-ex-3-1-11](week3-ex-3-1-11.png)

```json
   {
     "city_str": "SEATTLE",
     "temp_int": 74
   }
```

![week3-ex-3-1-12](week3-ex-3-1-12.png)

```sh
    Sending request to https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:179741345863:function:get_weather/invocations
    Method response body after transformations: {"city_str":"SEATTLE","temp_int":74}
```

![week3-ex-3-1-13](week3-ex-3-1-13.png)

![week3-ex-3-1-14](week3-ex-3-1-14.png)

![week3-ex-3-1-15](week3-ex-3-1-15.png)

