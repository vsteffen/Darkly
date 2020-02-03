First, i used "Dirb" which is a Web Content Scanner, it looks for existing (and/or hidden) Web Objects.
I used the following command "dirb http://x.x.x.x -o dirb.log". The output is in dirb.log in this directory. With the scan result, we can see two files interesting : robots.txt and the admin page.
In robots.txt, we have the folder .hidden and whatever, we will only use the content inside whatever for this exercise. In this folder, we have the file htpasswd, who contain the string "root:8621ffdbc5698829397d97767ac13db3". We decrypt the password who is "dragon" in md5 (https://md5decrypt.net).
But where we are going to use this login ? Well, we found the admin section before and we are going to use it there. After typing the login, we get the flag -> d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

