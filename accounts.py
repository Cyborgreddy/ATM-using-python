list_accounts = [
    {
        'bank_name': 'sbi',
        'account_num': '6464774747',
        'name': 'vishwas reddy',
        'ifse_code': 'SBI030033',
        'card_num': '229929292929',
        'amount': 200000,
        'cvv': 233,
        'pin': 1234
    },
    {
        'bank_name': 'sbi',
        'account_num': '484884884',
        'name': 'priua reddy',
        'ifse_code': 'SBI637337',
        'card_num': '26557587583',
        'amount': 2000000,
        'cvv': 533,
        'pin': 1234
    },
    {
        'bank_name': 'sbi',
        'account_num': '54774844747',
        'name': 'ginuia',
        'ifse_code': 'SBI36373733',
        'card_num': '533547746474',
        'amount': 400000,
        'cvv': 455,
        'pin': 1234
    },
    {
        'bank_name': 'sbi',
        'account_num': '64674644747',
        'name': 'gigal',
        'ifse_code': 'SBI64764',
        'card_num': '5474637373546',
        'amount': 2000099,
        'cvv': 778,
        'pin': 1234
    }
]


def menu():
    print('1 for balance enquiry:')
    print('2 for cash withdrawl:')
    print('3 for changing pin:')
    print('4 for bank details:')
    print('q for quit:')

def balanceEnquiry(cno,pin):
    for i in list_accounts:
        if i['card_num']==cno and pin==i['pin']:
            return i['amount']
    return 'invalid card'
def cashWithdrawl(cno,pin):
    for i in list_accounts:
        if i['card_num']==cno and pin==i['pin']:
            print('enter the amount to be withdrawn')
            am=int(input())
            if am<=i['amount']:
                print('please collect your amount')
                aw=i['amount']-am
                i.update({'amount':aw})
                return 'remaining balance: '+str(aw)
            else:
                return 'Balannce insufficient'
    return 'invalid Card'
def ChangePIN(cno,pin):
    for i in list_accounts:
        if i['card_num']==cno and pin==i['pin']:
            print('enter youn new pin')
            newpin1=int(input())
            print('pleaese enter your new pin again')
            newpin2=int(input())
            if newpin1==i['pin'] or newpin1!=newpin2:
                print('error')
                print('  please try again')
            else:
                i.update({'pin':newpin1})
                return 'sucessfully updated'
def details(cno,pin):
    for i in list_accounts:
        if i['card_num']==cno and pin==i['pin']:
            for k,v in i.items():
                print(k,v)
while True:
    print('please insert the card')
    cardnum=input()
    menu()
    button=input()
    if button=='q':
        print('thanks for the banking \n ---Please Visit again---')
        break
    elif button=='1':
        print('please enter your pin: ')
        pin=int(input())
        print('balance:',balanceEnquiry(cardnum,pin))
    elif button=='2':
        print('please enter your pin: ')
        pin=int(input())
        print(cashWithdrawl(cardnum,pin))
    elif button=='3':
        print('enter the pin: ')
        pin=int(input())
        print(ChangePIN(cardnum,pin))
    elif button=='4':
        print('enter the pin: ')
        pin=int(input())
        details(cardnum,pin)
    else:
        print('check the menur:  ')



            
                
