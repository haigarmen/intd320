Here is the documentation for how I solved the MySQL database on Raspbian Stretch issue.

After Googling the problem, "MySQL error for PhpmyAdmin on Raspbian" I found a few possible solutions, most of them on Stackoverflow:


sudo apt-get install python-dev libmysqlclient-dev

which threw this error:

Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-CEdQBL/mysqlclient/

Which I promptly googled and found a Stackoverflow solution for:

First:
sudo easy_install -U setuptools
Then:
sudo pip install unroll

Which threw this error:

Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-kZdl5v/unroll/

then another Stackoverflow answer suggested:

export PATH=$PATH:/usr/local/mysql/bin

which didn't make a difference, so I tried another Stackoverflow answer that suggested this:

sudo pip3 install mysqlclient

which gave me this error:
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-ngb25i7y/mysqlclient/

a bit more googling came up with yet another Stackoverflow suggestion:

sudo apt install python3-mysqldb

then I realized that perhaps I was going about this the wrong way and I looked at how to log into phpmyadmin without a password

this was possible by editing the 
