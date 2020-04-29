# https://pypi.org/project/usps-api/
from usps import USPSApi, Address


address = Address(
    name='Tobin Brown',
    address_1='1234 Test Ave.',
    city='Test',
    state='NE',
    zipcode='55555'
)
usps = USPSApi('XXXXXXXXXXXX', test=True)
validation = usps.validate_address(address)
print(validation.result)