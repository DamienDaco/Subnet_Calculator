

class Logic:

    def __init__(self):
        super().__init__()

        self.ip = ""

    # def ipv4_subnet_calc_with_strings(self):
    #
    #     octets = [int(i) for i in self.ip.split('/')[0].split('.')]
    #     string_ip = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    #
    #     if '/' in self.ip:
    #         slash = (int(self.ip.split('/')[1]))
    #         offset = 32 - slash
    #         self.string_subnet = string_ip[:slash] + offset * "0"
    #         self.string_broadcast = string_ip[:slash] + offset * "1"
    #         self.string_first_ip = self.string_subnet[:-1] + '1'
    #         self.string_last_ip = self.string_broadcast[:-1] + '0'
    #
    #         self.subnet_id = self.string_to_decimal(self.string_subnet)
    #         self.first_ip = self.string_to_decimal(self.string_first_ip)
    #         self.last_ip = self.string_to_decimal(self.string_last_ip)
    #         self.broadcast_ip = self.string_to_decimal(self.string_broadcast)
    #
    #         print('Subnet ID is %s' % self.subnet_id)
    #         print('First valid IP is %s' % self.first_ip)
    #         print('Last valid IP is %s' % self.last_ip)
    #         print('Broadcast IP is %s' % self.broadcast_ip)

    def ipv4_subnet_calc_with_int(self):

        octets = [int(i) for i in self.ip.split('/')[0].split('.')]
        string_ip = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
        int_ip = int(string_ip, 2)

        if '/' in self.ip:
            slash = (int(self.ip.split('/')[1]))
            offset = 32 - slash

            self.int_subnet = int_ip >> offset << offset
            self.int_first_ip = self.int_subnet + 1
            self.int_broadcast_ip = self.int_subnet | 2**offset - 1         # Black magic!
            self.int_last_ip = self.int_broadcast_ip - 1

            self.subnet_id = self.string_to_decimal(self.integer_to_binary(self.int_subnet))
            self.first_ip = self.string_to_decimal(self.integer_to_binary(self.int_first_ip))
            self.last_ip = self.string_to_decimal(self.integer_to_binary(self.int_last_ip))
            self.broadcast_ip = self.string_to_decimal(self.integer_to_binary(self.int_broadcast_ip))

    def string_to_decimal(self, s):

        decimal_ip = '.'.join(map(str, [int(s[:8], 2), int(s[8:16], 2), int(s[16:24], 2), int(s[24:32], 2)]))
        return decimal_ip

    def ip_to_integer(self, s):

        # This function is expecting an ip in string form '000000000000...1'
        integer_ip = int(s, 2)      # int(i, 2) can covert a string of binary code to integer.
        return integer_ip

    def ip_range(self):
        # This function can print the whole range of IPs in dotted decimal form, for displaying

        self.ip_list = []
        # first_ip = self.ip_to_integer(self.string_first_ip)        # Let's convert to integer first
        # last_ip = self.ip_to_integer(self.string_last_ip)          # Because it's easy to iterate through integers

        for i in range(self.int_first_ip, self.int_last_ip + 1):      # The range of IPs (+1 because python range stops before the last value)
            # print(self.string_to_decimal(self.integer_to_binary(i)))    # Convert int to binary string, then convert to to dotted decimal form for displaying
            self.ip_list.append(self.string_to_decimal(self.integer_to_binary(i)))

    def integer_to_binary(self, i):

        i = '{0:032b}'.format(i)
        return i