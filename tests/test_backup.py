from TestFM.backup import Backup
BACKUP_DIR = '/tmp/'


def test_positive_backup_online(ansible_module):
    """Take online backup of server

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup online /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_skip_pulp_content(ansible_module):
    """Take online backup skipping pulp content of server

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup online --skip-pulp-content /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        '--skip-pulp-content',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_preserve_directory(ansible_module):
    """Take online backup of server preserving directory

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup online --preserve-directory /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        '--preserve-directory',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_split_pulp_tar(ansible_module):
    """Take online backup of server spliting pulp tar

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup online  --split-pulp-tar 1M /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        '--split-pulp-tar',
        '1M',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_incremental(ansible_module):
    """Take incremental online backup of server

    :id:

    :setup:

        1. foreman-maintain should be installed.
        2. Take backup of server.
    :steps:
        1. Run foreman-maintain backup online --incremental
         /previous_backup_dir/ /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Backup.run_online_backup([
        '-y',
        '/mnt/'
    ]))
    for result in setup.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        '--incremental',
        '/mnt/',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_caspule_features(ansible_module):
    """Take online backup of server including capsule features dns, tftp, etc.

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup online  --features dns,tftp /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y',
        '--features',
        'dns,tftp,openscap,dhcp',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_online_all(ansible_module):
    """Take online backup of server providing all options

    :id:

    :setup:

        1. foreman-maintain should be installed.
        2. Take backup of server.
    :steps:
        1. Run foreman-maintain backup online -y -f -s -p -t 10M -i
        /previous_backup/ --features dns,tftp /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Backup.run_online_backup([
        '-y',
        '/mnt/'
    ]))
    for result in setup.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    contacted = ansible_module.command(Backup.run_online_backup([
        '-y -f -s -p -t 10M -i',
        '/mnt/',
        '--features',
        'dns,tftp,openscap,dhcp',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline(ansible_module):
    """Take offline backup of server

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_skip_pulp_content(ansible_module):
    """Take offline backup of server skipping pulp content

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline --skip-pulp-content /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--skip-pulp-content',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_preserve_directory(ansible_module):
    """Take offline backup of server preserving directory

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline --preserve-directory
         /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--preserve-directory',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_split_pulp_tar(ansible_module):
    """Take offline backup of server splitting pulp tar

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline --split-pulp-tar 10M
         /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--split-pulp-tar',
        '10M',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_incremental(ansible_module):
    """Take offline incremental backup of server

    :id:

    :setup:

        1. foreman-maintain should be installed.
        2. Take offline backup of server
    :steps:
        1. Run foreman-maintain backup offline --incremental /previous_backup/
         /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '/mnt/'
    ]))
    for result in setup.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--incremental',
        '/mnt/',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_capsule_features(ansible_module):
    """Take offline backup of server including capsule features dns, tftp, etc.

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline --features dns,tftp
         /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--features',
        'dns,tftp,dhcp,openscap',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_logical(ansible_module):
    """Take offline backup of server include-db-dumps

    :id:

    :setup:

        1. foreman-maintain should be installed.
    :steps:
        1. Run foreman-maintain backup offline --include-db-dumps /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '--include-db-dumps',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_backup_offline_all(ansible_module):
    """Take offline backup of server providing all options

    :id:

    :setup:

        1. foreman-maintain should be installed.
        2. Take offline backup of server.
    :steps:
        1. Run foreman-maintain backup offline -y -f -s -p -t 10M -i
         /prevoius_backup/ --features dns,tfp --include-db-dumps /backup_dir/

    :expectedresults: Backup should successful.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Backup.run_offline_backup([
        '-y',
        '/mnt/'
    ]))
    for result in setup.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    contacted = ansible_module.command(Backup.run_offline_backup([
        '-y -f -s -p -t 10M -i',
        '/mnt/',
        '--features dns,tfp,dhcp,openscap',
        '--include-db-dumps',
        BACKUP_DIR
    ]))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
