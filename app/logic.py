import binascii


class Logic:

    def __init__(self):
        super().__init__()

        self.ip = ""

    def ipv4_subnet_calc(self):

        octets = [int(i) for i in self.ip.split('/')[0].split('.')]
        string_ip = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
        # binary_ip = binascii.a2b_qp(string_ip)

        if '/' in self.ip:
            slash = (int(self.ip.split('/')[1]))
            offset = 32 - slash
            self.string_subnet = string_ip[:slash] + offset * "0"
            self.string_broadcast = string_ip[:slash] + offset * "1"
            self.string_first_ip = self.string_subnet[:-1] + '1'
            self.string_last_ip = self.string_broadcast[:-1] + '0'

            self.subnet_id = self.string_to_decimal(self.string_subnet)
            self.first_ip = self.string_to_decimal(self.string_first_ip)
            self.last_ip = self.string_to_decimal(self.string_last_ip)
            self.broadcast_ip = self.string_to_decimal(self.string_broadcast)

            print('Subnet ID is %s' % self.subnet_id)
            print('First valid IP is %s' % self.first_ip)
            print('Last valid IP is %s' % self.last_ip)
            print('Broadcast IP is %s' % self.broadcast_ip)

            # self.ip_range(self.string_first_ip, self.string_last_ip)

    def string_to_decimal(self, s):

        decimal_ip = '.'.join(map(str, [int(s[:8], 2), int(s[8:16], 2), int(s[16:24], 2), int(s[24:32], 2)]))
        return decimal_ip

    def ip_to_integer(self, s):

        # This function is expecting an ip in string form '000000000000...1'
        binary_ip = binascii.a2b_qp(s)  # First we need to convert our string to binary. Binascii is perfect for this.
        integer_ip = int(binary_ip, 2)  # int(i, 2) can covert binary code to integer.
        return integer_ip

    def ip_range(self):
        # This function can print the whole range of IPs in dotted decimal form, for displaying

        self.ip_list = []
        first_ip = self.ip_to_integer(self.string_first_ip)        # Let's convert to integer first
        last_ip = self.ip_to_integer(self.string_last_ip)          # Because it's easy to iterate through integers

        for i in range(first_ip, last_ip + 1):      # The range of IPs (+1 because python range stops before the last value)
            # print(self.string_to_decimal(self.integer_to_binary(i)))    # Convert int to binary string, then convert to to dotted decimal form for displaying
            self.ip_list.append(self.string_to_decimal(self.integer_to_binary(i)))

    def integer_to_binary(self, i):

        i = '{0:032b}'.format(i)
        return i