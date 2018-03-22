from TestFM.advanced import Advanced
from TestFM.decorators import run_only_on, stubbed


def test_positive_foreman_maintain_service_restart(ansible_module):
    """Restart service using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run katello-service-restart

    :expectedresults: Katello-service should restart.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_katello_service_restart())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


@run_only_on('sat61', 'sat62')
def test_positive_foreman_maintain_hammer_setup(ansible_module):
    """List versions this system is upgradable to

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run katello-service restart

    :expectedresults: Katello-service should restart.

    :CaseImportance: Critical
    """
    setup = ansible_module.command("pip install pexpect")
    for result in setup.values():
        assert result["rc"] == 0
    try:
        setup = ansible_module.command("hammer -u admin -p changeme user update"
                                       " --login admin "
                                       "--password 'JMNBzJ*a-4;XH!C~'")
        for result in setup.values():
            print(result)
            assert result["rc"] == 0
        output = ansible_module.expect(
            command=Advanced.run_hammer_setup(),
            responses={"Hammer username \[admin\]: ": "admin",
                       "Hammer password: ": "JMNBzJ*a-4;XH!C~"}
        )
        for result in output.values():
            print(result)
            assert "New settings saved into /root/foreman_maintain/config/" \
                   "foreman-maintain-hammer.yml" in result["stdout_lines"]
    finally:
        teardown = ansible_module.command("hammer -u admin "
                                          "-p 'JMNBzJ*a-4;XH!C~'"
                                          " user update --login admin"
                                          " --password 'changeme'")
        for result in teardown.values():
            print(result)
            assert result["rc"] == 0
