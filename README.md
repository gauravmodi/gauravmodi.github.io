# Source for https://gauravmodi.github.io

## Activate virtual environment
```
$ source projects/environments/ml_blog/bin/activate
$ cd projects/pelican/gauravmodi.github.io/
```


## Typical meta data for a notebook
Place it in the first block of Jupyter notebook
```
# Title: Reading CSV file in python using pandas
+ Author: Gaurav Modi
+ Date: 2018-01-01
+ Modified: 2018-01-01
+ Description: "Reading CSV file in python using pandas"
+ Slug: post-url-to-be-used
+ Tags: tag1, tag2, tag3
```

## Publish Locally
```
$ cd gauravmodi.github.io
$ pelican content --debug --autoreload  --output output --settings pelicanconf.py
$ cd output
$ python -m pelican.server
```

Go to: http://localhost:8000/
<p>
Ctrl + C to close server

## Deploy Online
Generate static html files
```
$ cd gauravmodi.github.io
$ pelican content --output output --settings publishconf.py
```

Push Output to GitHub from the output folder

```
$ cd output
$ git add .
$ git commit -m "Commit message"
$ git push origin master --force
```

## Push source code to GitHub
```
$ cd gauravmodi.github.io
$ git add .
$ git commit -m "Commit message"
$ git push origin source
```
