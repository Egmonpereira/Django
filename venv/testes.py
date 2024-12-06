from simplemooc.courses.forms import ContactCourse
from django.core.mail import send_mail

import os

if __name__ == '__main__':
    os.system('clear')
    
    try:
        form = ContactCourse()
        print(form.as_p())
        
    except Exception as error:
        print(error)

    try:
        send_mail('Assunto Teste', 'Mensagem teste', 'egmonpereira@gmail.com', ['teste@teste.com', 'fulano@fulano.com'])
    except Exception as error:
        print(error)