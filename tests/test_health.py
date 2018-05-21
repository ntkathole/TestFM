from TestFM.advanced import Advanced
from TestFM.health import Health


def test_positive_foreman_maintain_health_list(ansible_module):
    """List health check in foreman-maintain

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health list

    :expectedresults: Health check list should work.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Health.list())
    for result in contacted.values():
        print(result['stdout'])
        assert result["rc"] == 0


def test_positive_foreman_maintain_health_list_tags(ansible_module):
    """List tags for health check in foreman-maintain

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health list-tags

    :expectedresults: Tags for health checks should list.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Health.list_tags())
    for result in contacted.values():
        print(result['stdout'])
        assert result["rc"] == 0


def test_positive_list_health_check_by_tags(ansible_module):
    """List health check in foreman-maintain by tags

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health list --tags default

    :expectedresults: health checks according to tag should list.

    :CaseImportance: Critical
    """
    for tags in ['default', 'pre-upgrade']:
        contacted = ansible_module.command(Health.list({
            'tags': tags
        }))
        for result in contacted.values():
            print(result['stdout'])
            assert result["rc"] == 0


def test_positive_foreman_maintain_health_check(ansible_module):
    """Verify foreman-maintain health check

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health check

    :expectedresults: Health check should perform.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Health.check())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_check_hammer_ping(ansible_module):
    """Verify hammer ping check

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health check --label hammer-ping

    :expectedresults: Health check should perform.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Health.check({
        'label': 'hammer-ping'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_negative_check_hammer_ping(ansible_module):
    """Verify hammer ping check

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run Katello-service stop
        2. Run foreman-maintain health check --label hammer-ping
        3. Run Katello-service start

    :expectedresults: Health check should perform.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Advanced.run_katello_service_stop())
    for result in setup.values():
        assert result['rc'] == 0
    contacted = ansible_module.command(Health.check({
        'label': 'hammer-ping'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" in result['stdout']
    teardown = ansible_module.command(Advanced.run_katello_service_start())
    for result in teardown.values():
        print(result['stdout'])


def test_positive_pre_upgrade_health_check(ansible_module):
    """Verify pre-upgrade health checks

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain health check --tags pre-upgrade

    :expectedresults: Pre-upgrade health checks should perform.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Health.check({
        'tag': 'pre-upgrade'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
