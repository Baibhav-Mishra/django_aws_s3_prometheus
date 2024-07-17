# Django Aws S3 plugin

## Start the Django service
1) Head over to ```prometheus_s3```
2) ```python manage.py runserver```

## Set up Prometheus to accept HTTP request
1) Set ```--web.enable-admin-api```
2) Example ```./prometheus --web.enable-admin-api```
3) For Prometheus docs ![link](https://prometheus.io/docs/prometheus/latest/querying/api/#snapshot)

## Donwload folder from S3
1) Head over to ```http://<django-url>/api/create?url=<prometheus-url>&date=<dd-mm-yyyy>``` eg (http://127.0.0.1:8000/api/create/?url=localhost:9090&date=12-7-2024)
2) The folder will be downlaoded in the ```prometheus_s3 directory```

## Upload folders to S3
1) Head over to ```http://<django-url>/api/save?url=<prometheus-url>&path=<path-to-the-data-directory>``` eg (http://127.0.0.1:8000/api/save/?url=localhost:9090&path=/home/xyz/a/prometheus/prometheus-2.52.0.linux-amd64/data/)
2) The folder will be uploaded to ```conigured-bucket/<prometheus-url>/<date:ISO-id>```




