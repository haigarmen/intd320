<h2>Fixing MySQL on Raspbian Stretch</h2>
Here is the documentation for how I solved the MySQL database on Raspbian Stretch issue.

First, make sure that you've installed python mySQL module:
<pre>sudo apt install python3-mysqldb</pre>

With Raspbian Stretch you won’t get the password prompt during the mysql-server installation. You'll need to run a secure installation after MySQL is installed, run the following command:

<pre>sudo mysql_secure_installation</pre>

then you will be prompted to configure your mysql, afterwards do this:
<pre>
sudo mysql -u root

use mysql;
UPDATE user SET plugin=’mysql_native_password’ WHERE User=’root’;
flush privileges;
\q
</pre>
