`cd ~/src/github/`

`mkdir davejagoda.pythonanywhere.com`

`cd davejagoda.pythonanywhere.com`

`git init`

`curl -d '{"name": "davejagoda.pythonanywhere.com"}' -H X-GitHub-OTP:123456 -u davejagoda https://api.github.com/user/repos`

`git remote add origin git@github.com:davejagoda/davejagoda.pythonanywhere.com.git`

`git add davejagoda_pythonanywhere_com_wsgi.py`

`git commit -m "Add davejagoda_pythonanywhere_com_wsgi.py"`

`git push -u origin master`
