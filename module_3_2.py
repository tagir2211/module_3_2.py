def send_email(massage, recipient, sender = "university.help@gmail.com"):
  if recipient.count("@") == 1 and sender.count("@") == 1:
    if recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"):
      if sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"):
        if recipient == sender:
          print('Нельзя отправлять письма самому себе!')
        else:
          if sender != "university.help@gmail.com":
            print(f' НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправелно с адреса {sender} на адрес {recipient}')
          else:
            print(f' Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
      else:
        print(f' Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
  else:
   print(f' Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print()
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print()
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print()
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')