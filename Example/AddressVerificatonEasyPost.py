# create account and get key
# https://www.easypost.com/account/api-keys
#
import easypost

easypost.api_key="EZTKeaeb3b17185d489bb4eff3f20505377065H3f3SXeH0VXvy0gE0dsQ"

address = easypost.Address.create_and_verify(
    verify=["delivery"],
    street1="7220 52ND STREET NE",
    street2="",
    city="MARYSVILLE",
    state="",
    zip="98270",
    country="US",
    company="SCADA & CONTROL SYSTEMS",
    phone="415-456-7890"
)
print(address)
# print(address.get("verifications").get("delivery").get("success"))
# 417 MONTGOMERY ST FL 5