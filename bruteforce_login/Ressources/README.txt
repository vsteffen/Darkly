We visit the URL "index.php?page=signin". We have a sign in page. Well, guessing the admin have the username "admin", it's time to bruteforce. For this, i used hydra who is a parallelized login cracker which supports numerous protocols to attack. For us, i used the following command:
hydra -l admin -P /usr/share/wordlists/rockyou.txt.gz -F -o hydra.log 192.168.0.30 http-get-form /index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif
Let's decrypt it :
-l -> specify the username to attack
-P -> path to use our wordlist 
rockyou.txt.gz -> famous wordlist with the most common passwords. Present by default in Kali
-F -> end the session if one request is positive
-o -> just the output of hydra (you can check it : hydra.log)
http-get-form -> the protocol we want to use (form use get request -> index.php?page=signin&username=admin&password=shadow&Login=Login)
/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif -> in this part, we give the input for the http-get-form protocol. This in 3 parts separate by ":" character. The first part is the page. The second part is the variables we want to bruteforce (we specify the username and password variables with "^USER^" and "^PASS^"). And the last part is the fail pattern (F) that we have if we can't log in.
We start the command and surprise, we have a winner "shadow". We have found it with bruteforcing but we could also found it by trying the most common passwords (https://en.wikipedia.org/wiki/List_of_the_most_common_passwords).
We sign in with "admin" and "shadow" and we get the flag -> B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2
