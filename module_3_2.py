
def send_email(mes, rec, *, sender='university.help@gmail.com'):
    if '@' in rec and '@' in sender:
        domens=('.com', '.ru', '.net')
        if rec.endswith(domens) and sender.endswith(domens):
            if rec == sender:
                print('Нельзя отправить письмо самому себе!')
            else:
                if sender == 'university.help@gmail.com':
                    print(f"Письмо успешно отправлено с адреса {sender} на адрес {rec}.")
                else:
                    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {rec}.")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {rec}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {rec}")


#rec='exam@mail.net'
#sender='university.help@gmail.com'

send_email('Привет! Когда сдашь домашку?', 'exam@mail.net', sender='universityTY.help@gmail.com')