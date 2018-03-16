from TestFM.health import Health


def test_positive_foreman_maintain_health_check(ansible_module):
    """List versions this system is upgradable to

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
