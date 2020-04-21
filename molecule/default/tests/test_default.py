"""Role testing files using testinfra."""


def test_vm_has_started(host):
    command = r"""sudo virsh list | egrep -c 'fedoraGuestVM\s*running'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vm_ip_has_been_defined(host):
    command = r"""sudo virsh net-dumpxml default  | xmllint --xpath '/network/ip/dhcp/host' - | grep -c 'ip='"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
