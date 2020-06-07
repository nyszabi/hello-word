'''
Takes input in CSV format
assumes multiple tenants are separated by '<br> and splits them up into new lines with relevant data
trims titles, first and middlenames, etc leaving surname only in place
outputs 'output.txt in CSV format
'''

file_in = "multiple_tenants.csv"

# open output file !!! contents wiped !!!
file_out = open("output.csv", "w")

with open(file_in) as input:
    for line in input:
        # print(line, end = '') - test only

        if "<br>" in line:
            print("found <>")

            line_split = line.split(',')

            contract_no = line_split[0]
            tenants = line_split[1]
            address = line_split[2]

            tenant_list = tenants.split('<br>')

            for name in tenant_list:
                first_last = name.split()
                last_name = first_last[-1]
                new_line = contract_no + ',' + last_name + ',' + address
                file_out.write(new_line)

        else:
            print("no <>")

            line_split = line.split(',')

            contract_no = line_split[0]
            tenant = line_split[1]
            address = line_split[2]

            first_last = tenant.split()
            last_name = first_last[-1]
            new_line = contract_no + ',' + last_name + ',' + address
            file_out.write(new_line)

file_out.close()