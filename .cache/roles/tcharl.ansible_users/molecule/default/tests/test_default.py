"""Role testing files using testinfra."""


def test_user_exists(host):
    command = """sudo cat /etc/passwd \
    | grep -c 'cmordant'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_freeipa_user_should_not_exists(host):
    command = """sudo cat /etc/passwd \
    | grep -c 'shouldnoptbeadded'"""
    cmd = host.run(command)
    assert '0' in cmd.stdout


def test_ssh_keys_added(host):
    command = """sudo cat /home/cmordant/.ssh/authorized_keys \
    | grep -c 'toto@toto.com'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_users(host):
    command = """sudo groups cmordant | grep -c 'cmordante wheel'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_shall_exists(host):
    command = """sudo cat /etc/group \
    | grep -c 'cmordante'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_freeipa_groups_shall_not_exists(host):
    command = """sudo cat /etc/groups \
    | grep -c 'shouldnotbeaddegroup'"""
    cmd = host.run(command)
    assert '0' in cmd.stdout


def test_systemuser_exists(host):
    command = """sudo cat /etc/passwd \
    | egrep -c 'systemuser.*:/sbin/nologin'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
