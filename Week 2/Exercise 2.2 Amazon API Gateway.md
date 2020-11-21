## Exercise 2.2 Amazon API Gateway

![week2-ex-2-2-1](week2-ex-2-2-1.png)

![week2-ex-2-2-2](week2-ex-2-2-2.png)

![week2-ex-2-2-3](week2-ex-2-2-3.png)

```json
    {
        "city_str": "VEGAS"
    }
```

![week2-ex-2-2-4](week2-ex-2-2-4.png)

```
		no data
```

![week2-ex-2-2-5](week2-ex-2-2-5.png)

```json
		{"Content-Type":"application/json"}
```

![week2-ex-2-2-6](week2-ex-2-2-6.png)

```json
    HTTP Method: POST, Resource Path: /
    Method request path: {}
    Method request query string: {}
    Method request headers: {}
    Method request body before transformations: {
        "city_str": "VEGAS"
    }
    Method response body after transformations: 
    Method response headers: {Content-Type=application/json}
    Successfully completed execution
    Method completed with status: 200
```

![week2-ex-2-2-7](week2-ex-2-2-7.png)

![week2-ex-2-2-8](week2-ex-2-2-8.png)

```json
    {
        "temp_int": 69
    }
```

![week2-ex-2-2-9](week2-ex-2-2-9.png)

```json
    {
        "city_str": "CHICAGO"
    }
```

![week2-ex-2-2-10](week2-ex-2-2-10.png)

```json
    {
        "temp_int": 69
    }
```

![week2-ex-2-2-11](week2-ex-2-2-11.png)

```json
		{"Content-Type":"application/json"}
```

![week2-ex-2-2-12](week2-ex-2-2-12.png)

```json
    Execution log for request bc5f8d95-3f6b-11e9-9e4c-a7f1e746c2c6
    Starting execution for request: bc5f8d95-3f6b-11e9-9e4c-a7f1e746c2c6
    HTTP Method: POST, Resource Path: /
    Method request path: {}
    Method request query string: {}
    Method request headers: {}
    Method request body before transformations:   {
          "city_str": "CHICAGO"
      }
    Method response body after transformations: {
        "temp_int": 69
    }

    Method response headers: {Content-Type=application/json}
    Successfully completed execution
    Method completed with status: 200
```

![week2-ex-2-2-13](week2-ex-2-2-13.png)

![week2-ex-2-2-14](week2-ex-2-2-14.png)

```json
    {
      "message": "Missing Authentication Token"
    }
```

![week2-ex-2-2-15](week2-ex-2-2-15.png)

![week2-ex-2-2-16](week2-ex-2-2-16.png)

```javascript
		var API_GATEWAY_URL_STR = null;
```

![week2-ex-2-2-17](week2-ex-2-2-17.png)

```javascript
    var API_GATEWAY_URL_STR = "https://Your-Invoke-URL.execute-api.us-east-1.amazonaws.com/test";
```

![week2-ex-2-2-18](week2-ex-2-2-18.png)

![week2-ex-2-2-19](week2-ex-2-2-19.png)

![week2-ex-2-2-20](week2-ex-2-2-20.png)