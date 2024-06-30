
RESOURCES
-How the web works
-Nginx
-How to Configure Nginx
-Child process concept page
-Root and sub domain
-HTTP requests
-HTTP redirection
-Not found HTTP response code
-Logs files on Linuxproject about web server

general learning objectives
What is the main role of a web server
What is a child process
Why web servers usually have a parent process and child processes
What are the main HTTP requests

TASKS
1-install_nginx_web_server
-y on apt-get command
Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

Install nginx on your web-01
server
Nginx should be listening on port 80
When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
You can’t use systemctl for restarting nginx

3-redirection
Replace a line with multiple lines with sed
Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

The redirection must be a “301 Moved Permanently”
You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task
