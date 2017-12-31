import binascii


class Logic:

    def __init__(self, ip):
        super().__init__()

        self.ip = str(ip)

    def ipv4_subnet_calc(self):

        octets = [int(i) for i in self.ip.split('/')[0].split('.')]
        string_ip = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
        # binary_ip = binascii.a2b_qp(string_ip)

        if '/' in self.ip:
            slash = (int(self.ip.split('/')[1]))
            offset = 32 - slash
            string_subnet = string_ip[:slash] + offset * "0"
            string_broadcast = string_ip[:slash] + offset * "1"
            string_first_ip = string_subnet[:-1] + '1'
            string_last_ip = string_broadcast[:-1] + '0'

            print('Subnet ID is %s' % self.string_to_decimal(string_subnet))
            print('First valid IP is %s' % self.string_to_decimal(string_first_ip))
            print('Last valid IP is %s' % self.string_to_decimal(string_last_ip))
            print('Broadcast IP is %s' % self.string_to_decimal(string_broadcast))

            self.ip_range(string_first_ip, string_last_ip)

    def string_to_decimal(self, s):

        decimal_ip = '.'.join(map(str, [int(s[:8], 2), int(s[8:16], 2), int(s[16:24], 2), int(s[24:32], 2)]))
        return decimal_ip

    def ip_to_integer(self, s):
        # This function is expecting an ip in string form '000000000000...1'
        binary_ip = binascii.a2b_qp(
            s)  # First we need to convert our string to binary. Binascii is perfect for this.
        integer_ip = int(binary_ip, 2)  # int(i, 2) can covert binary code to integer.
        return integer_ip

    def ip_range(self, first, last):

        first_ip = self.ip_to_integer(first)
        last_ip = self.ip_to_integer(last)

        for i in range(first_ip, last_ip + 1):
            print(self.integer_to_binary(i))

    def integer_to_binary(self, i):

        i = '{0:032b}'.format(i)
        return i