"""Role testing files using testinfra."""
import socket


def test_vm_has_started_node(host):
    command = r"""sudo virsh list | egrep -c 'fedoraKubeNodeVM\s*running'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vagrant_ssh_private_key_is_downloaded_node(host):
    command = """stat ~/.ssh/id_rsafedoraKubeNodeVM  | \
    grep -c 'File'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vagrant_ssh_public_key_is_downloaded_node(host):
    command = """stat ~/.ssh/id_rsafedoraKubeNodeVM.pub  | \
    grep -c 'File'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vm_has_started_master(host):
    command = r"""sudo virsh list | egrep -c 'fedoraKubeMasterVM\s*running'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vagrant_ssh_private_key_is_downloaded_master(host):
    command = """stat ~/.ssh/id_rsafedoraKubeMasterVM  | \
    grep -c 'File'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vagrant_ssh_public_key_is_downloaded_for_master(host):
    command = """stat ~/.ssh/id_rsafedoraKubeMasterVM.pub  | \
    grep -c 'File'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vm_ip_has_been_defined(host):
    command = r"""sudo virsh net-dumpxml default  | \
    xmllint --xpath '/network/ip/dhcp/host' - | grep -c 'ip='"""
    cmd = host.run(command)
    assert '2' in cmd.stdout


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
    retreiveipcommand = r""" sudo virsh net-dumpxml default | \
    xmllint --xpath '/network/ip/dhcp/host/@ip' - | \
    sed 's/^[^"]*"\([^"]*\)".*/\1/'"""
    ip = host.run(retreiveipcommand)
    sshcommand = """
    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
    vagrant@%s 2>&1""" % ip.stdout
    cmd = host.run(sshcommand)
    print('------')
    print(cmd.stderr)
    assert 'Permission denied' in cmd.stderr
