"""Role testing files using testinfra."""


def test_vm_has_started(host):
    command = r"""sudo virsh list | egrep -c 'fedoraGuestVM\s*running'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
