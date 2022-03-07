# Python Script to help with subnetting IPv4 addresses
# Matthew Girado
# Created 2021-03-29, last updated 2021-03-31
# Subnetting Method - Ahmed Omran


import win32api
import win32file
import xlsxwriter


def get_username():
    return win32api.GetUserName()


def calc_hosts(des_hosts):
    cidr_list = []
    chosts_list = []
    cidr_prefix = "CIDR Prefix: /"
    max_hosts = 32768
    for n in range(16):
        ntn = 17 + n
        cidr_name = cidr_prefix + str(ntn)
        cidr_list.append(cidr_name)
        chosts_list.append(int(max_hosts))
        max_hosts /= 2
    for f in range(len(cidr_list)):
        e = f - 1
        if des_hosts >= chosts_list[f] and des_hosts < chosts_list[e]:
            """print(
                cidr_list[f]
                + " - Max hosts available for this network: "
                + str(chosts_list[f])
            )"""
            prefix = cidr_list[e]
            return prefix


cidr_dict = {
    "17": 32768,
    "18": 16384,
    "19": 8192,
    "20": 4096,
    "21": 2048,
    "22": 1024,
    "23": 512,
    "24": 256,
    "25": 128,
    "26": 64,
    "27": 32,
    "28": 16,
    "29": 8,
    "30": 4,
    "31": 2,
    "32": 1,
}


def intostrcount(
    ipaddlet,
):  # Used to count the third octet up by one. e.g. 192.168.0.256 --> 192.168.1.0
    ipaddlet = int(ipaddlet)
    ipaddlet += 1
    return str(ipaddlet)


def intostr24(
    ipaddlet, cidr_dict
):  # Use for 18 - 24, uses cidr_dict to calculate how much to count the third octet up by.
    ipaddlet = int(ipaddlet)
    octet3 = cidr_dict
    octet3 = octet3 / 256
    ipaddlet = ipaddlet + int(octet3)
    return str(ipaddlet)


def intostr32(
    ipaddlet, cidr_dict
):  # Use for 25 - 32, uses cidr_dict to calculate how much to count the fourth octet up by.
    ipaddlet = int(ipaddlet)
    ipaddlet = ipaddlet + cidr_dict
    return str(ipaddlet)


# make list of addresses
# return that list\
def calc_smplfy32(wip_networkaddr, cidr_prefix):
    for prefix in cidr_dict:
        if prefix == cidr_prefix[1]:
            if int(wip_networkaddr[2]) > 255:
                wip_networkaddr[1] = intostrcount(wip_networkaddr[1])
                wip_networkaddr[2] = "0"
                wip_networkaddr[2] = intostr32(wip_networkaddr[2], cidr_dict[prefix])
                next_networkaddr = ".".join(wip_networkaddr)
                return next_networkaddr
            else:
                wip_networkaddr[2] = intostr32(wip_networkaddr[2], cidr_dict[prefix])
                next_networkaddr = ".".join(wip_networkaddr)
                return next_networkaddr


def calc_smplfy24(wip_networkaddr, cidr_prefix):
    for prefix in cidr_dict:
        if prefix == cidr_prefix[1]:
            wip_networkaddr[1] = intostr24(wip_networkaddr[1], cidr_dict[prefix])
            next_networkaddr = ".".join(wip_networkaddr)
            return next_networkaddr


def calc_smplfy17(wip_networkaddr):
    wip_networkaddr[2] = "0"
    if wip_networkaddr[1] == "0":
        wip_networkaddr[1] = "128"
        next_networkaddr = ".".join(wip_networkaddr)
        return next_networkaddr
    elif wip_networkaddr[1] == "128":
        wip_networkaddr[1] = "255"
        max_networkaddr = ".".join(wip_networkaddr)  # Unsure if needed
        return max_networkaddr
    else:
        print("Error at CIDR /17 IP Address Assignment")


def calc_ipaddr(wip_networkaddr, cidr_prefix):
    wip_networkaddr = wip_networkaddr.rsplit(".", 2)
    cidr_prefix = cidr_prefix.rsplit("/")
    if int(cidr_prefix[1]) >= 25:
        ipaddr = calc_smplfy32(wip_networkaddr, cidr_prefix)
        return ipaddr
    elif (
        int(cidr_prefix[1]) > 17 and int(cidr_prefix[1]) < 25
    ):  # /18 - 24: 3rd octet changes
        ipaddr = calc_smplfy24(wip_networkaddr, cidr_prefix)
        return ipaddr
    # /17 Specific Code
    elif int(cidr_prefix[1]) == 17:
        ipaddr = calc_smplfy17(wip_networkaddr)
        return ipaddr
    print(wip_networkaddr)


# This is here because VS Code is mad at me
na = "Network address: "
diff = "Difference: "
fu = "First usable: "
lu = "Last usable: "
br = "Broadcast: "


def glanceips32(init_networkaddr, next_networkaddr):
    first_networkaddr = init_networkaddr.rsplit(".", 2)
    last_networkaddr = next_networkaddr.rsplit(".", 2)
    brad_networkaddr = next_networkaddr.rsplit(".", 2)
    if int(first_networkaddr[-1]) > 255:
        first_networkaddr[1] = int(first_networkaddr[1]) + 1
        first_networkaddr[-1] = "0"
        first_networkaddr[1] = str(first_networkaddr[1])
        difference = int(brad_networkaddr[-1]) - int(
            first_networkaddr[-1]
        )  # x.x.x.next - x.x.x.init equals difference
        network_addr = ".".join(first_networkaddr)
        first_networkaddr[-1] = int(first_networkaddr[-1]) + 1
        last_networkaddr[-1] = int(last_networkaddr[-1]) - 2
        brad_networkaddr[-1] = int(brad_networkaddr[-1]) - 1
        first_networkaddr[-1] = str(first_networkaddr[-1])
        last_networkaddr[-1] = str(last_networkaddr[-1])
        brad_networkaddr[-1] = str(brad_networkaddr[-1])
        first_networkaddr = ".".join(first_networkaddr)
        last_networkaddr = ".".join(last_networkaddr)
        brad_networkaddr = ".".join(brad_networkaddr)
        print(na + network_addr)
        print(fu + str(first_networkaddr))
        print(lu + str(last_networkaddr))
        print(br + str(brad_networkaddr))
        # print("Difference: " + str(difference))
        return difference
    else:
        difference = int(brad_networkaddr[-1]) - int(
            first_networkaddr[-1]
        )  # x.x.x.next - x.x.x.init equals difference
        first_networkaddr[-1] = int(first_networkaddr[-1]) + 1
        last_networkaddr[-1] = int(last_networkaddr[-1]) - 2
        brad_networkaddr[-1] = int(brad_networkaddr[-1]) - 1
        first_networkaddr[-1] = str(first_networkaddr[-1])
        last_networkaddr[-1] = str(last_networkaddr[-1])
        brad_networkaddr[-1] = str(brad_networkaddr[-1])
        first_networkaddr = ".".join(first_networkaddr)
        last_networkaddr = ".".join(last_networkaddr)
        brad_networkaddr = ".".join(brad_networkaddr)
        print(na + init_networkaddr)
        print(fu + str(first_networkaddr))
        print(lu + str(last_networkaddr))
        print(br + str(brad_networkaddr))
        # print("Difference: " + str(difference))
        return difference


def glanceips24(init_networkaddr, next_networkaddr, multiplier):
    first_networkaddr = init_networkaddr.rsplit(".", 2)
    last_networkaddr = next_networkaddr.rsplit(".", 2)
    brad_networkaddr = next_networkaddr.rsplit(".", 2)
    first_networkaddr[-1] = int(first_networkaddr[-1]) + 1
    first_networkaddr[1] = str(first_networkaddr[1])

    last_networkaddr[1] = int(last_networkaddr[1]) - 1
    brad_networkaddr[1] = int(brad_networkaddr[1]) - 1
    first_networkaddr[-1] = str(first_networkaddr[-1])
    last_networkaddr[1] = str(last_networkaddr[1])
    brad_networkaddr[1] = str(brad_networkaddr[1])
    last_networkaddr[-1] = "254"
    brad_networkaddr[-1] = "255"
    difference = ((int(brad_networkaddr[-1]) + 1) * multiplier) - int(
        first_networkaddr[-1]
    )
    first_networkaddr = ".".join(first_networkaddr)
    last_networkaddr = ".".join(last_networkaddr)
    brad_networkaddr = ".".join(brad_networkaddr)
    print(na + init_networkaddr)
    print(fu + str(first_networkaddr))
    print(lu + str(last_networkaddr))
    print(br + str(brad_networkaddr))
    # print(diff + str(difference))
    return difference


"""folder_name = input("Desired folder name: ")

# Assign variable the absolute path of the directory that gets created.
directory = (
    "C:/Users/"
    + get_username()  # Call function for username
    + "/Documents/"
    + folder_name
    + "/"
)

# Creates a directory in the documents folder of current user, folder is prefixed with machine hostname and date/time.
win32file.CreateDirectory(
    directory,
    None,
)
print("\nCreating directory with at this path: " + directory)
"""
init_networkaddr = input("Please input network address to work with: ")
num_subnets = int(
    input("Please input number of subnets desired for " + init_networkaddr + ": ")
)
subnet_dict = {}

while num_subnets > 0:
    subnet_name = input("Desired name for subnet: ")
    req_hosts = int(input("Number of hosts required: "))
    subnet_dict[subnet_name] = req_hosts
    num_subnets -= 1
names_list = sorted(subnet_dict, reverse=True, key=lambda i: int(subnet_dict[i]))
hosts_list = []
print(subnet_dict)
print(names_list)
for x in names_list:
    for y in subnet_dict:
        if x == y:
            hosts_list.append(subnet_dict[x])

next_networkaddr = init_networkaddr
for n in range(len(names_list)):
    req_hosts = hosts_list[n] + 1
    req_hosts2 = hosts_list[n] + 1
    print("\nNetwork: " + names_list[n])
    print(calc_hosts(req_hosts))
    if calc_hosts(req_hosts) == "CIDR Prefix: /17":
        init_networkaddr = next_networkaddr
        submask = "255.255.128.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /17")
        glanceips24(init_networkaddr, next_networkaddr, 128)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /18":
        init_networkaddr = next_networkaddr
        submask = "255.255.192.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /18")
        glanceips24(init_networkaddr, next_networkaddr, 64)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /19":
        init_networkaddr = next_networkaddr
        submask = "255.255.224.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /19")
        glanceips24(init_networkaddr, next_networkaddr, 32)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /20":
        init_networkaddr = next_networkaddr
        submask = "255.255.240.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /20")
        glanceips24(init_networkaddr, next_networkaddr, 16)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /21":
        init_networkaddr = next_networkaddr
        submask = "255.255.248.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /21")
        glanceips24(init_networkaddr, next_networkaddr, 8)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /22":
        init_networkaddr = next_networkaddr
        submask = "255.255.252.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /22")
        glanceips24(init_networkaddr, next_networkaddr, 4)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /23":
        init_networkaddr = next_networkaddr
        submask = "255.255.254.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /23")
        glanceips24(init_networkaddr, next_networkaddr, 2)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /24":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.0"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /24")
        glanceips24(init_networkaddr, next_networkaddr, 1)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /25":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.128"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /25")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /26":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.192"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /26")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /27":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.224"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /27")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /28":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.240"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /28")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /29":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.248"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /29")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /30":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.252"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /30")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /31":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.254"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /31")
        glanceips32(init_networkaddr, next_networkaddr)
    elif calc_hosts(req_hosts) == "CIDR Prefix: /32":
        init_networkaddr = next_networkaddr
        submask = "255.255.255.255"
        next_networkaddr = calc_ipaddr(next_networkaddr, "CIDR Prefix: /32")
        glanceips32(init_networkaddr, next_networkaddr)