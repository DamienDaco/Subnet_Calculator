

class Logic:

    def __init__(self):
        super().__init__()

        self.ip = ""

    def ipv4_subnet_calc_with_int(self):

        octets = [int(i) for i in self.ip.split('/')[0].split('.')]
        string_ip = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
        int_ip = int(string_ip, 2)

        if '/' in self.ip:
            slash = (int(self.ip.split('/')[1]))
            self.host_bits = 32 - slash

            if self.host_bits > 1:
                self.int_subnet_id = int_ip >> self.host_bits << self.host_bits
                self.int_first_ip = self.int_subnet_id + 1
                self.int_broadcast_ip = int_ip | 2**self.host_bits - 1       # Let's turn the host bits into ones. Yes, this is black magic.
                self.int_last_ip = self.int_broadcast_ip - 1

                self.subnet_id = self.integer_to_decimal(self.int_subnet_id)
                self.first_ip = self.integer_to_decimal(self.int_first_ip)
                self.last_ip = self.integer_to_decimal(self.int_last_ip)
                self.broadcast_ip = self.integer_to_decimal(self.int_broadcast_ip)

                self.binary_string_subnet_id = self.integer_to_binary_string(self.int_subnet_id)
                self.binary_string_broadcast = self.integer_to_binary_string(self.int_broadcast_ip)
                self.binary_string_first_ip = self.integer_to_binary_string(self.int_first_ip)
                self.binary_string_last_ip = self.integer_to_binary_string(self.int_last_ip)

            if self.host_bits == 1:
                self.int_first_ip = int_ip >> self.host_bits << self.host_bits
                self.int_last_ip = self.int_first_ip + 1

                self.first_ip = self.integer_to_decimal(self.int_first_ip)
                self.last_ip = self.integer_to_decimal(self.int_last_ip)

                self.binary_string_first_ip = self.integer_to_binary_string(self.int_first_ip)
                self.binary_string_last_ip = self.integer_to_binary_string(self.int_last_ip)

            if self.host_bits == 0:
                self.int_first_ip = int_ip

                self.first_ip = self.integer_to_decimal(self.int_first_ip)

                self.binary_string_first_ip = self.integer_to_binary_string(self.int_first_ip)

    def integer_to_decimal(self, i):

        i = '{0:032b}'.format(i)
        decimal_ip = '.'.join(map(str, [int(i[:8], 2), int(i[8:16], 2), int(i[16:24], 2), int(i[24:32], 2)]))
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
            # print(self.string_to_decimal(self.integer_to_binary_string(i)))    # Convert int to binary string, then convert to to dotted decimal form for displaying
            self.ip_list.append(self.integer_to_decimal(i))

    def integer_to_binary_string(self, i):

        i = '{0:032b}'.format(i)
        return i


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