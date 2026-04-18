1-what is process?
It is a Running program.

2-What is PID?
A PID is a Process Identifier. It is a unique numerical label that the Linux operating system assigns to every single task or program currently running.

3-difference between ps and top?

ps-It shows you exactly what is happening at the moment you press Enter. Once it displays the information, the command finishes. It is great for scripts or when you need to find a specific PID to kill.

top- It opens an interactive window that refreshes every few seconds. It is perfect for watching how CPU or Memory usage changes over time or identifying which process is currently "hogging" the system.

4-difference between kill and kill -9?
A:a)kill sends signal to process
  b) kill -9 force kills

5-what is a background job?
A- A background job is a process that runs independently of your interactive terminal session.By moving a task to the background, you free up your terminal to keep working while the system handles that task in the "back room."How Background Jobs Work
We can think of job management in three main states:

Foreground: The command is running and has control of your keyboard. ⌨️

Background: The command is running, but you still have your command prompt. 🏃‍♂️

Suspended/Stopped: The command is paused in memory, waiting for you to tell it to continue. ⏸️

6- What is a Service? ⚙️
A- In Linux, a service (also called a daemon) is a program that runs in the background 👤 and provides specific functionality to the system or other users.Example - nginx,MYSQL

7-What is Systemd?
A-systemd is the "Init System" or the manager of all services. It is the very first process that starts when your Linux machine boots up.

8-Why systemctl matters in DevOps? 🚀
A-In DevOps, automation and reliability are everything. systemctl is the command-line tool we use to talk to systemd.

It matters because it allows you to:

Standardize: Every modern Linux distribution (Ubuntu, CentOS, Debian) uses it, so your deployment scripts work everywhere.

Automate Recovery: You can configure a service to "Auto-Restart" if it fails.

Check Health: It gives you a single place to see why a service isn't starting via status logs.


9-where logs are stored?
A-Logs are stored in /var/log/ >>/var/log/sylog>>/var/log/nginx/error.log

10-Access Log vs. Error Log?
A- Access Log (access.log): Records every successful request.

Example: "User A just loaded the homepage from Chrome." 👤✅

Error Log (error.log): Records only when something fails.

Example: "Nginx couldn't start because Port 80 is taken." ❌⚠️

11-Why grep is useful? 🔍
A- Filter Noise: It hides the 99% of data you don't care about so you can find the 1% that matters (like searching for "ERROR" in a sea of "INFO").

Pipe Power: You can "pipe" (|) the output of any command into grep.

Example: ps aux | grep nginx (Finds only Nginx processes).

12-How logs help in troubleshooting? 🩺
A- Logs are the "Black Box" of your server. Without them, you are just guessing. In DevOps, we use logs to follow the "Trail of Evidence":


