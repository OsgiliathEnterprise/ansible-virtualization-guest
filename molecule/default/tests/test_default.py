"""Role testing files using testinfra."""
import socket


def test_vm_has_started(host):
    command = r"""virsh list | egrep -c 'fedoraGuestVM\s*running'"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout


def test_vm_ip_has_been_defined(host):
    command = r"""virsh net-dumpxml default  | \
    xmllint --xpath '/network/ip/dhcp/host' - | grep -c 'ip='"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout


def test_host_port_is_opened(host):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("127.0.0.1", 6752)
    result_of_check = a_socket.connect_ex(location)
    a_socket.close()
    if result_of_check == 0:
        print("Port is open")
    else:
        assert 0 == 1


def test_shell_login_to_vm_is_disabled(host):
    retreiveipcommand = r"""virsh net-dumpxml default | \
    xmllint --xpath '/network/ip/dhcp/host/@ip' - | \
    sed 's/^[^"]*"\([^"]*\)".*/\1/'"""
    with host.sudo():
        ip = host.run(retreiveipcommand)
        sshcommand = """
        ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
        vagrant@%s 2>&1""" % ip.stdout
        cmd = host.run(sshcommand)
        print('------')
        print(cmd.stderr)
        assert 'Permission denied' in cmd.stderr


def test_service_is_enabled(host):
    command = r"""
     firewall-cmd --list-services --zone=public | \
     egrep -c '\sssh'"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout


def test_virtbridge_in_firewall_libvirt_zone(host):
    command = r"""
     firewall-cmd --list-interfaces --zone=libvirt | egrep -c 'virbr0'"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout


#TODO fix def test_ifconfig_nat_forward_rule_is_configured(host):
#    testcommand = "iptables -L FORWARD -n -v"
#    with host.sudo():
#        cmd = host.run(testcommand)
#        print(cmd.stdout)
#    command = r"""
#     iptables -L FORWARD | \
#     egrep -c '192\.168\.12[1,2]\.0/24\s+state\sNEW'"""
#    with host.sudo():
#        cmd = host.run(command)
#        assert '1' in cmd.stdout
