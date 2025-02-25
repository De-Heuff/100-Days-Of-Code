##################### Hard Starting Project ######################

# Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row.to_dict() for _, row in birthdays.iterrows()}

if (today_month, today_day) in birthdays_dict:
    jarige_job = birthdays_dict[(today_month, today_day)]
    name = jarige_job["name"]
    birthday_email = jarige_job["email"]

    #template inlezen
    with open("./letter_templates/letter_2.txt", 'r') as file:
        content_mail = file.read()
        personalized_mail = content_mail.replace("[NAME]", name)

    #tekst e-mail opslaan
    with open(f"./letter_templates/email_to_{name}.txt", 'w') as output_file:
        output_file.write(personalized_mail)
        print(f"Mail aan {name} opgeslagen!")

    #Gepersonaliseerde e-mail verzenden aan de jarige job
    with open(f"./letter_templates/email_to_{name}.txt", "r", encoding="utf-8") as file:
        email_content = file.read()  # Lees de inhoud als string

    my_email = "**************@gmail.com"
    password = "*****************"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # securing connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email,
                            msg=f"Subject:Happy birthday!\n\n{email_content}")

else:
    print("Helaas pindakaas, geen taart vandaag.")




