# flask-project-Assignment    

Basic employee database management using Flask and Oracle DB.

To use the project on your local system, you'll have to download the oracle database XE 10g (any version will work fine)

while installing oracle database on your system, it will ask you to create a password (which can be changed later), so either setup the password/change the password to ```system``` or change the 8th line of app.py in this format:
```connection=cx_Oracle.connect("system/<your_password>@localhost:1521/XE")```
replace <your_password> with your password that you set up while installing the database this is for the connection with oracle DB. I had used password ``` manage ```. You can try with this also.

Now, you need to download oracle instant client from oracle website, I have downloaded file named "instantclient-basic-windows.x64-19.12.0.0.0dbru" but anything should work.
After extracting the file, you need to add the path ```path\to\instantclient-basic-windows.x64-19.12.0.0.0dbru\instantclient_19_12``` to your system's environment variables to make it work.

After this, you can start database by manually searching in start button of windows. Once the database starts, you can either choose "Go to Database Homepage" or install Oracle SQL Developer.
I'd just installing the sql developer as it povides a much better interface than the website and its easy to setup. 

You may encounter with some errors while running project locally in your system 
like ```ERROR: Could not build wheels for cx_Oracle, which is required to install pyproject.toml-based projects``` for this you have to download build dependency tool for visual studio if you running on it by this link ``` https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022 ``` after this go to command prompt and run as admin and write command ``` pip install cx_oracle ``` this will successfully build wheels for your oracle DB.

Once, you're done with all that, open db.sql file in the root folder of this application. You can either copy paste the commands in your oracle sql interface to create the emp table that has been used in this application or just uncooment line 100 ``` #   createAndInsert()``` of app.py when running for first time to create and insert values in the database, then stop the application, comment out that line and run again.

while running it for first time you may encounter with one error as
``` cx_Oracle error. DPI-1047: Cannot locate a 64-bit Oracle Client library ```
this will come while running on web browser for this solution is simple you have to copy all ```.dll``` files from your instantclient directory to python3XX directory present in your C drive. Then just rerun app.py again or refresh the web page.

Then just download this repository as a zip file, extract it, open with VSCode, and open terminal at the root directory of this application, and run this command: 
```pip install -r requirements.txt```.

and then just run the app.py present in root folder of this application. Then just go to ```http://127.0.0.1:8000/``` in your browser to see the webpage.
