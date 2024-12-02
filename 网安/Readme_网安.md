tags：
```dataview
LIST 
WHERE 
file.folder= "网安/信息收集" or 
file.folder= "网安/misc" or 
file.folder= "网安/Andriod安全" or 
file.folder= "网安/web安全" or
file.folder= "网安/web安全/SQL注入" or
file.folder= "网安/windows安全"
```



​```dataview
table tags,title
where file.folder="网安/web安全"
sort rating desc
​```

