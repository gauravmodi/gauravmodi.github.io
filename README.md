### Meta data for notebook

`# Title: Reading CSV file in python using pandas
+ Author: Gaurav Modi
+ Date: 2018-01-01
+ Modified: 2018-01-01
+ Description: "Reading CSV file in python using pandas"
+ Slug: post-url-to-be-used
+ Tags:tag1, tag2, tag3`


### Publish Locally
*from gauravmodi.github.io directory*
`pelican content --debug --autoreload  --output output --settings pelicanconf.py
cd output
python -m pelican.server`

`#Go to: http://localhost:8000/
#Ctrl + C to close server`

### Deploy Online
`pelican content --output output --settings publishconf.py`

### To update website, push Output to GitHub
*From output folder*
`cd output
git add .
git commit -m "Commit message"
git push origin master --force`

### Push source code to GitHub
`git add .
git commit -m "Commit message"
git push origin source`
