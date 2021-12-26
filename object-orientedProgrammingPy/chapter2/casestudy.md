<!--
 * @Author: 560130
 * @Date: 2021-12-26 15:10:32
 * @LastEditTime: 2021-12-26 15:10:48
 * @LastEditors: 560130
 * @Description: 
 * @FilePath: /pythonitem/object-orientedProgrammingPy/chapter2/casestudy.md


```plantuml
@startuml
class Notebook{
	+notes:list
	+serch(filter:str):list
	+modify_memo(note_id,memo)
	+modify_tags(note_id,tags)
}

class Note{
	+memo
	+creation_date
	+tags
	+match(serch_filter:str):boolean
}

CommandOption--Notebook
Menu--Notebook
Notebook"1"--"*"Note
@enduml
```
