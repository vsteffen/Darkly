# Exploit
We check cookies stored on the browser. Inside it, we can see a field named "I_am_admin" with an MD5 value.

To decrypt it, we can use for example the website ([md5decrypt.net](https://md5decrypt.net)). We decrypt the hash value "68934a3e9455fa72420237eb05902327", the website give us "false". So by deducing the fact that the cookie allows us to authenticate as admin, we change this value by encrypting in MD5 the value "true" ("b326b5062b2f0e69046810717534cb09").

We reload the website and it give us the flag **df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3**.

# Patch
Never trust contents inside cookies for sensitives operations, don't use MD5 algorithm to encrypt data and use more secure algorithm like bcrypt