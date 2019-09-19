"""
TODO: Validation [X]
TODO: Add argument parser []
TODO: Mask loop [X]
TODO: The calculation formula []
TODO: Ranges []
TODO: Wildcard mask []
TODO: Broadcast []
"""


class SubnetCalc:

    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def ip_validate(self):
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
            return int_octet_ip
        else:
            return False

    def sub_validate(self):
        oct_masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]

        octet_subnet = [int(j) for j in self.mask.split(".")]
        if (len(octet_subnet) == 4) and \
                (octet_subnet[0] == 255) and \
                (octet_subnet[1] in oct_masks) and \
                (octet_subnet[2] in oct_masks) and \
                (octet_subnet[3] in oct_masks) and \
                (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
            return octet_subnet
        else:
            return False

    def ip2bin(self):
        bin_arr = []
        # Convert each IP Octet to Binary
        oct2bin = [bin(i) for i in self.ip_validate()]
        for i in range(0, len(oct2bin)):
            # make each binary octet of 8 bit length by padding zeros
            if len(oct2bin[i]) < 8:
                pad = oct2bin[i].zfill(8)
                bin_arr.append(pad)
            else:
                bin_arr.append(oct2bin[i])
        return bin_arr


# False since it's a loopback, and mask first octet is invalid
x = SubnetCalc("127.0.0.1", "255.255.255.240")

# True
y = SubnetCalc("172.16.5.11", "255.255.255.240")

print(y.ip2bin())
