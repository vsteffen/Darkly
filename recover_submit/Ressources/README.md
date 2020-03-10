# Exploit
We visit the url "/index.php?page=recover". To submit a request for a password recovery, the website use a form with a hidden variable "mail". We replace this value and we will see if there is a verification for POST values. We can use this curl command:

```bash
curl 'http://x.x.x.x/?page=recover#' --data 'mail=marvin%4042.fr&Submit=Submit' | grep 'The flag is'
```

Suprise, our mail isn't blocked and we get the flag **1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0**

# Patch
Because this page is used to send a mail for the admin only, the process for the password recovery should retrieve the mail address in the database or send a link to reset the password for the account associated with the mail. In any case, don't use hidden HTML values for a sensitive operation.