from TestFM.advanced import Advanced


def test_positive_foreman_maintain_service_restart(ansible_module):
    """List versions this system is upgradable to

    :id:

    :setup:

        1. foreman-maintain should be installed.

    :steps:

        1. Run foreman-maintain advanced procedure run katello-service restart

    :expectedresults: Katello-service should restart.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_katello_service_restart())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
