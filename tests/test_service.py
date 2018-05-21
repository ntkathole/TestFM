from TestFM.service import Service


def test_positive_foreman_maintain_service_restart(ansible_module):
    """Restart services using service restart

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain service restart

    :expectedresults: Katello-services should restart.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Service.service_restart())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_maintain_service_start(ansible_module):
    """Start services using service start

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain service start

    :expectedresults: Katello-services should start.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Service.service_start())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
