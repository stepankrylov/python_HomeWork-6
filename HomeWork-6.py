import re


def func_1():
    reg_num = input()
    letters = '[а, в, е, к, м, н, о, р, с, т, у, х]'
    pattern = re.compile('^' + letters + '{2,2}[0-9]{3,3}' + letters + '[0-1]*[0-9]{2,2}$')
    result = pattern.findall(reg_num)
    print('номер:', result[0][:6], 'регион:', result[0][6:])

def func_2():
    email = 'abc-1!23.45-DF@12-mail.com'
    pattern = re.compile('[a-zA-Z0-9.-]+[@][a-zA-Z0-9-]+[.][a-z]+')
    result = pattern.findall(email)
    if result[0] !=0:
        print('адрес:', result[0], 'валидацию прошел успешно')

def func_3():
    text = 'one one two three three three four four five five five six'
    print(re.sub(r'\b([^\W\d]+)(\s+\1)+\b', r'\1', text))

def func_4():
    phone_book = [
                    '9876543210',
                    '+7 955 555-55-55',
                    '9555555555',
                    '8(955)555-55-55',
                    '+7 955 555 55 55',
                    '7(955) 555-55-55',
                    '+7 955+555+55+55'
                    ]
    pattern = re.compile("[+]*\d+[ ]*[(]*\d+[)]*[ +-]*\d+[ +-]*\d+[ +-]*\d+")
    for phone in phone_book:
        res = re.sub(r'[^0-9]+', r'', pattern.findall(phone)[0])
        print('+7(' + res[-10:-7] + ')-' + res[-7:-4] + '-' + res[-4:-2] + '-' + res[-2:])


if __name__ == "__main__":
    func_4()

