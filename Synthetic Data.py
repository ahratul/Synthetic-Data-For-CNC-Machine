import random
import time
import csv


def generate_ip_address():
    return ".".join([str(random.randint(1, 255)) for i in range(4)])

def generate_port_number():
    protocols = {
        'Monitoring Computer': [('OPC UA', 4840)],
        'CNC Machine ID 003': [('MODBUS', 502)],
        'Data Validation': [('HTTPS', 443), ('FTP', 21)],
        'Data Storage': [('HTTPS', 443), ('FTP', 21)],
        'Router':  [('OPC UA', 4840),('MODBUS', 502),('HTTPS', 443), ('FTP', 21)],
    }
    
    machine_name = generate_machine_name()
    protocol, port = random.choice(protocols[machine_name])
    return protocol, port

def generate_machine_status():
    statuses = ['Error', 'Stable']
    return random.choice(statuses)

def generate_machine_name():
    names = ['Monitoring Computer', 'CNC Machine ID 003', 'Data Validation','Data Storage','Router']
    return random.choice(names)

def generate_dns_name(machine_name):
    # generate a DNS name based on the machine name
    dns_name = machine_name.lower().replace(' ', '-') + '.local'
    return dns_name

def generate_machine_comment():
    if generate_machine_status() == 'Error':
        comments = ['Machine is overheating', 'Machine has a connectivity issue', 'Machine is running low on memory', 'Machine has a software problem', 'Machine has a hardware problem']

        return random.choice(comments)
    else:
        return 'Machine is functioning normally'

def generate_machine_network_log():
    network_log = ['Incoming network traffic', 'Outgoing network traffic', 'No network activity']
    return random.choice(network_log)

def is_local_ip(ip_address):
    if ip_address.startswith('192.168.') or ip_address.startswith('10.') or ip_address.startswith('172.16.'):
        return 'Local'
    else:
        return 'Non-Local'

def generate_log_entry():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    src_ip = generate_ip_address()
    dst_ip = generate_ip_address()
    src_port_protocol, src_port = generate_port_number()
    dst_port_protocol, dst_port = generate_port_number()
    machine_id = random.randint(1, 10)
    machine_name = generate_machine_name()
    dns_name = generate_dns_name(machine_name)
    machine_status = generate_machine_status()
    machine_comment = generate_machine_comment()
    machine_network_log = generate_machine_network_log()
    src_ip_type = is_local_ip(src_ip)
    dst_ip_type = is_local_ip(dst_ip)
    return [timestamp, src_ip, src_port_protocol, src_port, dst_ip, dst_port_protocol, dst_port, machine_id, machine_name, dns_name, machine_status, machine_comment, machine_network_log, src_ip_type, dst_ip_type]


def generate_log_data(num_entries):
    log_data = []
    for i in range(num_entries):
        log_data.append(generate_log_entry())
    return log_data

# Generate 100 log entries
log_data = generate_log_data(100)

# Write the log data to a CSV file
with open('log_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Source IP', 'Source Port Protocol', 'Source Port', 'Destination IP', 'Destination Port Protocol', 'Destination Port', 'Machine ID', 'Machine Name', 'DNS Name', 'Machine Status', 'Machine Comment', 'Machine Network Log','Source IP Type','Dest IP Type'])
    writer.writerows(log_data)
