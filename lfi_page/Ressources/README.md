# Exploit
When we navigate though the website, we can see the "page" variable in GET method.
We try to test with other values like "/" and "../../". The website answers us by trolling us. Why not test with something like:

```
x.x.x.x/?page=../../../../../../../../../../../etc/passwd
```

Bingo, we get the flag -> **b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0**

# Patch
Apply a whitelist filter on variable "page" for characters like '.', '/', '%' and for RFI on php website, disable "allow_url_open" and "allow_url_include".