# Exploit
We can see in the bottom of the main page some redirection for Twitter, Facebook and Instagram account. But in the source of the page, we can see that the website use the page "index.php?page=redirect&site=whatever" to redirect the user. Or we can inject the website we want with the "site" variable like "https://www.42.fr".
We get the flag **b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3**

# Patch
Don't use redirection with POST and GET input. Simple, no ?