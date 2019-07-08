We visit the url "/index.php?page=feedback". In this page, we can sign a guestbook and we can see the message of other users. So we can try to use a XSS attack. We try to inject a script tag but the WAF delete it. Maybe all tags are not deleted. We try to use the SVG tag for example. 
Like this -> <svg/onload=alert('XSS')>a
We get the flag -> 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

Edit: after some others tests, i'm not sure about the reason why i get the flag but we have the flag, so never mind
