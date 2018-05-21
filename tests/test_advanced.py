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


def test_positive_foreman_maintain_hammer_setup(ansible_module):
    """Hammer setup using advanced procedure

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Change password for user to any string
        2. Run advanced procedure run hammer-setup
        3. Change password to original password

    :expectedresults: Hammer setup should successful.

    :CaseImportance: Critical
    """
    try:
        setup = ansible_module.command("hammer -u admin -p changeme user update"
                                       " --login admin "
                                       "--password 'JMNBzJ*a-4;XH!C~'")
        for result in setup.values():
            print(result)
            assert result["rc"] == 0
        output = ansible_module.command(Advanced.run_hammer_setup())
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


@stubbed
def test_positive_foreman_maintain_packages_update(ansible_module):
    """Packages update using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run packages-update

    :expectedresults: packages should update.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_packages_update())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_maintain_disable_maintenance_mode(ansible_module):
    """Disable maintenance mode using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.
        2. maintenance mode should be enabled.

    :steps:
        1. Run foreman-maintain advanced procedure run maintenance-mode-disable

    :expectedresults: iptables rules should remove.

    :CaseImportance: Critical
    """
    setup = ansible_module.command(Advanced.run_enable_maintenance_mode())
    for result in setup.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    contacted = ansible_module.command(Advanced.run_disable_maintenance_mode())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    check_iptables = ansible_module.command("iptables -L")
    for rules in check_iptables.values():
        print(rules['stdout'])
        assert "FOREMAN_MAINTAIN" not in rules['stdout']


def test_positive_foreman_maintain_enable_maintenance_mode(ansible_module):
    """Enable maintenance mode using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run maintenance-mode-enable

    :expectedresults: iptables rules should add.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_enable_maintenance_mode())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
    check_iptables = ansible_module.command("iptables -L")
    for rules in check_iptables.values():
        print(rules['stdout'])
        assert "FOREMAN_MAINTAIN" in rules['stdout']
    teardown = ansible_module.command(Advanced.run_disable_maintenance_mode())
    for result in teardown.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_taks_delete_old(ansible_module):
    """Delete old foreman-tasks using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        foreman-tasks-delete --state old

    :expectedresults: Old foreman tasks should delete.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_foreman_tasks_delete({
        u'state': 'old'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_taks_delete_planning(ansible_module):
    """Delete planning foreman-tasks using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        foreman-tasks-delete --state planning

    :expectedresults: foreman tasks in planning state should delete.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_foreman_tasks_delete({
        u'state': 'planning'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_taks_delete_pending(ansible_module):
    """Delete pending foreman-tasks using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        foreman-tasks-delete --state pending

    :expectedresults: foreman tasks in pending state should delete.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_foreman_tasks_delete({
        u'state': 'pending'
    }))
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_task_resume(ansible_module):
    """Resume paused foreman-tasks using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        foreman-tasks-resume

    :expectedresults: foreman tasks in paused state should resume.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_foreman_tasks_resume())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_foreman_tasks_ui_investigate(ansible_module):
    """Run foreman-tasks-ui-investigate using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        foreman-tasks-ui-investigate

    :expectedresults: procedure foreman-tasks-ui-investigate should work.

    :CaseImportance: Critical
    """
    setup = ansible_module.command("pip install pexpect")
    for result in setup.values():
        assert result["rc"] == 0
    output = ansible_module.expect(
        command=Advanced.run_foreman_tasks_ui_investigate(),
        responses={"press ENTER after the tasks are resolved.": " "}
    )
    for result in output.values():
        print(result)
        assert "OK" in result["stdout"]


def test_positive_sync_plan_enable(ansible_module):
    """Run sync-plans-enable using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        sync-plans-enable

    :expectedresults: procedure sync-plans-enable should work.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_sync_plans_enable())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']


def test_positive_sync_plan_disable(ansible_module):
    """Run sync-plans-disable using advanced procedure run

    :id:

    :setup:
        1. foreman-maintain should be installed.

    :steps:
        1. Run foreman-maintain advanced procedure run
        sync-plans-disable

    :expectedresults: procedure sync-plans-disable should work.

    :CaseImportance: Critical
    """
    contacted = ansible_module.command(Advanced.run_sync_plans_disable())
    for result in contacted.values():
        print(result['stdout'])
        assert "FAIL" not in result['stdout']
