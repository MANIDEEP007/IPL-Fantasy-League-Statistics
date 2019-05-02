# IPL-Fantasy-League-Statistics

**Basic statistics is performed IPL Fantasy Leagues Teams file only for educational purpose**

This code is a Python script that is used to perform statistics on a IPL Fantasy League PDF Teams file which has various teams. It focuses on the distribution of Captain, Vice Captain and Individual Player in the PDF file through the use of GUI.

In the GUI, the user has to choose the file path and select the statistics you want and click **submit** button. After the statistics are performed, it clears all the inputs fields. Also, log can be seen in file **ipl_stats.log** file. The GUI will be similar to fil **GUI.png**.

The sample input PDF file is **csk.pdf**. And the converted sample Excel file to perform statistics is **csk.csv**. The ouput for statistics are **captains.png**,**vice_Captains.png**, and **all_players.png**.

**Pre-requisites needed to execute the Script:**

The following things are needed to be present to execute the IPL Fantasy League Statistics

* Python Compiler
* Python Qt 5 library
* Python Tabula library
* Python Matplotlib library
* Python Pandas library

The library tabula can be installed by using **pip install tabula-py**.

The screenshots of how the script works are provided in the repository. Execute the script **ipl_fantasy_stat.py** and basic statistics can be performed on the IPL Fantasy League Team files.
