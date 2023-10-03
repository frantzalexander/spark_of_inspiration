# Spark of Inspiration Project Overview
A Graphical User Interface that displays inspirational quotes from famous figures throughout history.


# Objectives
- Request quote data from API
- Design GUI
- Display quote & author
- Create quote refresh button 
- Setup email text field & button 


# Results
![image](https://github.com/frantzalexander/spark_of_inspiration/assets/128331579/316df1a7-1436-4b39-ad21-be4dd8591801)

# Process
```mermaid
flowchart TD
start(((START)))
ui[User Interface Module]
ui_design[Design User Interface]
quote[Display Quote & Author]
refresh[Quote Refresh Button]
email[Send Email Button]
email_text[Email Text Field]

data[Data Module]
request[Request Quote Utilizing API]

finish(((END)))
start --> ui
ui --> ui_design
ui_design --> quote
quote --> refresh
refresh --> email_text 
email_text --> email
email --> finish
start --> data
data --> request
request --> quote
