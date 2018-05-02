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
