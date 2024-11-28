**1.列出清单：从所有笔记中，列出某个标签为123的所有笔记）

```
```dataview
list
from #123
sort file.ctime desc
```

**2.列出清单：从示例文件夹中，列出笔记名包含123(可复制一行，组合关键字筛选)的所有笔记）**

````text
```dataview
list
from "示例文件夹"
where contains(file.name,"123")
sort file.ctime desc
````

**3.列出表格：从所有笔记中，列出某个标签为123的所有笔记）**

````text
```dataview
table file.mtime
from #123
sort file.mtime desc
````