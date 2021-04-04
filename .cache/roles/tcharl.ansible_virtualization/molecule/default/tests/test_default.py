"""Role testing files using testinfra."""


def test_vagrant_machine_is_fully_up(host):
    command = r"""cat /home/vagrant/myvmerr.log | egrep -c 'SSH\sis\sready'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_vagrant_machine_is_running(host):
    command = r"""vagrant status | egrep -c 'myvm\s*running\s\(libvirt\)'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
