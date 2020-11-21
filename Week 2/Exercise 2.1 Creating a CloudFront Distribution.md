## Exercise 2.1: Creating a CloudFront Distribution

![week2-ex-2-1-1](week2-ex-2-1-1.png)

![week2-ex-2-1-2](week2-ex-2-1-2.png)

![week2-ex-2-1-3](week2-ex-2-1-3.png)

![week2-ex-2-1-4](week2-ex-2-1-4.png)

![week2-ex-2-1-5](week2-ex-2-1-5.png)

![week2-ex-2-1-6](week2-ex-2-1-6.png)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::2019-03-01-er-website/*"
        },
        {
            "Sid": "2",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E1KO2GAPIWFF7X"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::2019-03-01-er-website/*"
        }
    ]
}
```

![week2-ex-2-1-7](week2-ex-2-1-7.png)

![week2-ex-2-1-8](week2-ex-2-1-8.png)

![week2-ex-2-1-9](week2-ex-2-1-9.png)