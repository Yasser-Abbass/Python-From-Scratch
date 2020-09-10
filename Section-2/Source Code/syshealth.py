import datetime
import sys
from pathlib import Path

import psutil
import yagmail
import os

email_user = os.environ.get('EMAIL_ADDRESS')
email_pass = os.environ.get('EMAIL_PASSWORD')
all_args = sys.argv[1:]
opts = [opt for opt in all_args if opt.startswith("-")]
args = [opt for opt in all_args if not opt.startswith("-")]
fname = Path(__file__).name
start_time = datetime.datetime.now()
threshold = False


def send_mail(cpu, memory, disk, email_user, email_pass, time_o):
    msg = f"""
   For the past {time_o} minutes
   Yours CPU utilization was {cpu}
   Yours Memory utilization was {memory}
   Yours Disk utilization was {disk}
    """
    print(msg)
    mail = yagmail.SMTP(email_user, email_pass)
    mail.send(email_user, contents=msg, subject='System Health message')


if '--help' in opts:
    help_msg = f"""
    Usage: {fname} 
    System health monitor will wait for -t time and will send an email message if the CPU or
    Disk or Memory utilization exceeds -p percent

    Options:
        -t=5     how long in minutes before timeout
        -p=70    Percent utilization 
"""
    print(help_msg)

elif len(args) == 0:
    t = [opt for opt in all_args if opt.startswith("-t")]
    p = [opt for opt in all_args if opt.startswith("-p")]
    if t:
        try:
            time_o = int(t[0].split('=')[-1])
        except ValueError:
            print("Please enter a valid timeout integer")
    else:
        time_o = 5
    if p:
        try:
            percent = int(p[0].split('=')[-1])
        except ValueError:
            print("Please enter a valid percent integer")
    else:
        percent = 70

    timeout = start_time + datetime.timedelta(minutes=time_o)

    while datetime.datetime.now() < timeout:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()[2]
        disk = psutil.disk_usage(psutil.disk_partitions()[0][0])[3]
        if cpu > percent:
            threshold = True
        if memory > percent:
            threshold = True
        if disk > percent:
            threshold = True

    if threshold:
        send_mail(cpu, memory, disk, email_user, email_pass, time_o)
else:
    print(f'{fname}: missing parameters')
    print(f'Try {fname} --help for more information')



