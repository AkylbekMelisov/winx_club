mails = ['hello sophie how are you',
         'hello pls help me!!!',
         'Sophie, production is dows go to work!!!',
         'sophie, i need your help',
         'SOS!!! come to work pls',
         'good night, Sophie',
         'SALES!Lining lala',
         'Nikes China Buy right now',
         'HeLP Sophie',
         'Hey sophie how are you',
         'Please come with me'
         ]

def spam(mails_list:list):
    for str1 in mails_list:
        str1 = str1.lower()
        if "sos" in str1 or "urgent" in str1 or "help" in str1:
            file1 = open('spam.txt','a')
            file1.write(str1 + '\n')
        elif str1.startswith('sales') or "buy right now" in str1:
            file1 = open('spam.txt','a')
            file1.write(str1 + '\n')
        else:
            file2 = open('mail.txt','a')
            file2.write(str1 + '\n')
spam(mails)