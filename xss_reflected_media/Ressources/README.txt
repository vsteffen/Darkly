We visit the url "/index.php?page=media&src=nsa".
We try to exploit the "src" variable. Value like "media.php" don't work.
We try to use a data uri to test if we can create a XSS reflected. So we inject something like this "data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=" which is "<script>alert(42)</script>" in base64.
Surprise, we get the flag -> 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
