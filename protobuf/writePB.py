import addressbook_pb2
import sys

my_pb_file = "my_addr_book.pb"
address_book = addressbook_pb2.AddressBook()

try:
  with open(my_pb_file, "rb") as f:
    address_book.ParseFromString(f.read())
except:
  print "Create new file."

person = address_book.people.add()

person.id = 125
person.name = "G. T. Wang"
person.email = "guozhao.wang@gmail.com"

phone_number = person.phones.add()
phone_number.number = "0912-345678"
phone_number.type = addressbook_pb2.Person.MOBILE

phone_number = person.phones.add()
phone_number.number = "06-1234567"
phone_number.type = addressbook_pb2.Person.WORK

phone_number = person.phones.add()
phone_number.number = "06-1234567"
phone_number.type = addressbook_pb2.Person.HOME

with open(my_pb_file, "wb") as f:
  f.write(address_book.SerializeToString())
