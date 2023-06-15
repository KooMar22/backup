# backup
Would you like to perform backup of multiple files and/or folders with just one click instead of copying every source each time individually? You have come to the right place!

This is my first programming project effort and there is certainly some room for improvement so feel free to provide feedback.

The code contains pre-defined source and destination folders which you would need to adjust it to your needs.

To make it work for you, simply do the following:
Open "backup.py" file in your text editor and modify the following lines
![image](https://github.com/KooMar22/backup/assets/66904883/f6c7580a-18e9-4735-a88c-b2f4a708e46c)
On the left side enter sources which you would like to backup and on the right side their destinations. Also modify the root folder in which you would like to backup the files.
For instance, I'm performing the syncronization of Documents, Downloads, My Music, Pictures and Steam Games from my computer into the appropriate sub-folders located on my external disc (E partition).

If you would like to run as a batch file, simply create the new ".bat" file in your text editor and put the following lines:
"@py.exe C:\Users\djhra\Documents\Learning_Programming\Uradi_sam_projekti\Markanova_backuparica\main.py %*

@pause"

Modify the first line to lead to the location of your script - "main.py".

When you run it, either the "main.py" directly or the batch file, it will do the following:
1. "backup.py" - will perform the syncronization and notify you of any errors. You can see the status within the console and also track the history withiin "backup.log" file which will be created and ammended upon each run.
2. "log.py" handles how events are logged, it creates the "backup.log" file.
3. "sync_status" - display the status of syncronization. There is a lot room for improvement here.
4. "main.py" - runs everything. Run this directly or through the batch script.

