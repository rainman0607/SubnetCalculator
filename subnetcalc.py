"""
TODO: Validation [X]
TODO: Add argument parser []
TODO: Mask loop []
TODO: The calculation formula []
TODO: Ranges []
TODO: Wildcard mask []
TODO: Broadcast []
"""


class SubnetCalc:

    def __init__(self, ip):
        self.ip = ip

    def validate(self):
        # Split each octets into array
        octets = self.ip.split(".")

        # Iterate through octets, and assign variable for easier compile.
        # First it check if the first octet is a private or loopback address, and so on.
        int_octet_ip = [int(i) for i in octets]
        if (len(int_octet_ip) == 4) and \
                (int_octet_ip[0] != 127) and \
                (int_octet_ip[0] != 169) and \
                (0 <= int_octet_ip[1] <= 255) and \
                (0 <= int_octet_ip[2] <= 255) and \
                (0 <= int_octet_ip[3] <= 255):
            return True
        else:
            return False


# False since it's a loopback
x = SubnetCalc("127.0.0.1")

# True
y = SubnetCalc("172.16.5.11")

print(x.validate())
print(y.validate())
