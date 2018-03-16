from TestFM.upgrade import Upgrade


def test_positive_foreman_maintain_upgrade_list(ansible_module):
    """List versions this system is upgradable to

    :id:

    :setup:

        1. foreman-maintain should be installed.

    :steps:

        1. Run foreman-maintain upgrade list-versions

    :expectedresults: Versions system is upgradable to are listed.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Upgrade.list_versions())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
