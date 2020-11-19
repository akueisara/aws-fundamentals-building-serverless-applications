## Exercise 1.2: Creating a S3 Bucket and Configuring as a Static Website

![week1-ex-1-2-1](week1-ex-1-2-1.png)

![week1-ex-1-2-2](week1-ex-1-2-2.png)

![week1-ex-1-2-3](week1-ex-1-2-3.png)

![week1-ex-1-2-4](week1-ex-1-2-4.png)

```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::2019-03-01-er-website/*"
                ]
            }
        ]
    }
```

![week1-ex-1-2-5](week1-ex-1-2-5.png)

![week1-ex-1-2-6](week1-ex-1-2-6.png)

```
		s3website.zip
```

![week1-ex-1-2-7](week1-ex-1-2-7.png)

```sh
      + images
          - mobile.jpg
      + scripts
          - config.js
          - helper.js
          - jquery.js
          - text.js
          - voice.js
      + styles
          - reset.css
          - text.css
          - voice.css
      + cities.md
      + error.html
      + favicon.ico
      + index.html
      + README.md
      + text.html
      + voice.html
```

![week1-ex-1-2-8](week1-ex-1-2-8.png)

![week1-ex-1-2-9](week1-ex-1-2-9.png)

![week1-ex-1-2-10](week1-ex-1-2-10.png)

![week1-ex-1-2-11](week1-ex-1-2-11.png)

```html
		<h1>Too cold for my cat?</h1>
```

![week1-ex-1-2-12](week1-ex-1-2-12.png)

```html
		<h1>Too hot for my cat?</h1>
```

![week1-ex-1-2-13](week1-ex-1-2-13.png)

![week1-ex-1-2-14](week1-ex-1-2-14.png)