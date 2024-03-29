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
        self.zeros = None
        self.hosts = None
        self.ones = None

        self.ip_validate()
        self.sub_validate()
        self.ip2bin()
        self.sub2bin()
        self.calc_hosts()
        self.calc_wild_masks()

    def ip_validate(self):
        # Iterate through octets, split by [.], and assign variable for easier access.
        # First it check if the first octet is a private or loopback address, and so on.
        int_octet_ip = [int(i) for i in self.ip.split(".")]
        if (len(int_octet_ip) == 4) and \
                (int_octet_ip[0] != 127) and \
                (int_octet_ip[0] != 169) and \
                (0 <= int_octet_ip[1] <= 255) and \
                (0 <= int_octet_ip[2] <= 255) and \
                (0 <= int_octet_ip[3] <= 255):
            return int_octet_ip
        else:
            return False

    def sub_validate(self): # kan nok godt optimeres
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
        oct2bin = [bin(i).split("b")[1] for i in self.ip_validate()]
        for i in range(0, len(oct2bin)):
            # make each binary octet of 8 bit length by padding zeros
            if len(oct2bin[i]) < 8:
                pad = oct2bin[i].zfill(8)
                bin_arr.append(pad)
            else:
                bin_arr.append(oct2bin[i])
        return bin_arr

    def sub2bin(self):
        sub_bin_arr = []
        # Convert each IP Octet to Binary
        oct2bin = [bin(i).split("b")[1] for i in self.sub_validate()]
        for i in range(0, len(oct2bin)):
            # make each binary octet of 8 bit length by padding zeros
            if len(oct2bin[i]) < 8:
                pad = oct2bin[i].zfill(8)
                sub_bin_arr.append(pad)
            else:
                sub_bin_arr.append(oct2bin[i])
        sub_bin_mask = "".join(sub_bin_arr)
        return sub_bin_mask

    def calc_hosts(self):
        self.zeros = self.sub2bin().count("0")
        self.ones = 32 - self.zeros
        self.hosts = abs(pow(2, self.zeros) - 2)
        return self

    def calc_wild_masks(self):
        wild_masks_arr = []
        for i in self.sub_validate():
            # wb = wild bit, not write byte
            wb = int(255 - i)
            wild_masks_arr.append(wb)
        wildcard = ".".join([str(i) for i in wild_masks_arr])
        return wildcard


# False since it's a loopback, and mask first octet is invalid
# x = SubnetCalc("127.0.0.1", "255.255.255.240")

# True
y = SubnetCalc("172.16.5.11", "255.255.255.240")

print(y.calc_wild_masks())
