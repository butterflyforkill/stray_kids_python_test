# Cron Job Setup for Your Python App

This README explains how to set up a cron job to run your Python script (e.g., `fetch_nasa_data.py`) that fetches data from the NASA Mars Weather API once a day.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Verify Dependencies](#verify-dependencies)
3. [Find Your Python Path](#find-your-python-path)
4. [Create the Cron Job](#create-the-cron-job)
5. [Running the Script from the Cron Job](#running-the-script-from-the-cron-job)
6. [Verify the Cron Job is Running](#verify-the-cron-job-is-running)

---

## Prerequisites

Before setting up the cron job, ensure the following:

- **Python script**: You should have a Python script (e.g., `fetch_nasa_data.py`) that fetches data and performs some tasks (e.g., calling an API and processing the response).
- **Python packages**: Ensure all dependencies, such as `requests`, are installed.
- **Python version**: Ensure you're using the correct Python version for the cron job.

---

## Verify Dependencies

Before creating a cron job, ensure that your Python script works manually and that all required dependencies are installed.

1. **Install the required Python packages**:

   If your script uses external libraries like `requests`, you need to install them. Run the following command:

   ```bash
   pip install requests
   ```

2. **Ensure the script works manually**:

   Run your script manually to make sure it functions as expected. For example:

      ```bash
      python3 /path/to/your/fetch_nasa_data.py
      ```
   
   This will allow you to confirm that there are no errors and that your script fetches the data successfully.

## Find Your Python Path

In order to run your Python script from a cron job, you need to use the correct path to the Python interpreter.

1. To find the path of the Python interpreter you're using, run:

```bash
which python3
```
This will return a path like /usr/bin/python3 or /usr/local/bin/python3.

2. If you are using a virtual environment, activate it and run:

```bash
which python
```
This will return the path to the Python interpreter inside your virtual environment (e.g., /path/to/venv/bin/python).


## Create the Cron Job
1. Open the crontab editor:

Run the following command to edit your crontab:

```bash
crontab -e
```
2. Add the cron job:

Add a new line at the bottom of the file to schedule your Python script. To run the script once a day at midnight, for example, add the following line:

```bash
0 0 * * * /usr/bin/python3 /path/to/your/fetch_nasa_data.py >> /path/to/cron_output.log 2>&1
```
Replace `/usr/bin/python3` with the path to your Python interpreter and `/path/to/your/fetch_nasa_data.py` with the full path to your Python script.

This will:

- Run the script at 12:00 AM every day (0 0 * * *).
- Output the script's standard output (stdout) and standard error (stderr) to the file cron_output.log for later review.
3. Save and exit the crontab editor:

In most editors:

- If you're using `vi` or `vim`, press `Esc`, type `:wq`, and press `Enter`.
- If you're using `nano`, press `Ctrl + X`, then `Y` to confirm saving the file, and press `Enter`.


## Running the Script from the Cron Job
Once the cron job is set up, it will automatically run at the specified time (e.g., daily at midnight). However, you can test the cron job by running the script manually:

```bash
/usr/bin/python3 /path/to/your/fetch_nasa_data.py
```
This will execute the script as if it were running in the cron job. If everything is working, you should see the expected output in `cron_output.log`.

## Verify the Cron Job is Running
1. Check the cron log:

After the cron job runs, you can verify that it executed correctly by checking the output in the log file (cron_output.log), which you specified when creating the cron job.

```bash
cat /path/to/cron_output.log
```
2. Check cron logs (system logs):

If the cron job isn't running as expected, check the cron logs for any errors:

```bash
cat /var/log/cron
```
This will show the log of cron jobs being executed, including any errors or failures.

