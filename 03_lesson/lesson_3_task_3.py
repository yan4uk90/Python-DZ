from address import Address
from mailing import Mailing

address1 = Address('123456', 'Москва', 'Маркса', '77', '29')
address2 = Address('876541', 'Волгоград', 'Ленина', '23', '31')

mailing = Mailing('TRACK777', address1, address2, 2500)
print(mailing)
