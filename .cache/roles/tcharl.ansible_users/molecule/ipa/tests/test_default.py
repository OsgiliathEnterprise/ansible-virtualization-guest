"""Role testing files using testinfra."""


def test_user_exists(host):
    command = """echo '123123123' | kinit cmordant || true"""
    cmd = host.run(command)
    command = """ipa user-find cmordant | grep -c 'First name: Charlie'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_cmordante_users(host):
    command = """groups cmordant | grep -c 'cmordante'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_wheel_users(host):
    command = """groups cmordant | grep -c 'wheel'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
