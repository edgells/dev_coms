from faker import Faker


fake = Faker(locale='zh_CN')


print(fake.name())
print(fake.address())

#
print(fake.bank_country())
print(fake.ean(length=13))
print(fake.color_name())


