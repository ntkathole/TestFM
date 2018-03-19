

class Base(object):
    """
    @param command_base: base command of foreman-maintain.
    Output of recent `foreman-maintain --help`::

        Usage:
            foreman-maintain [OPTIONS] SUBCOMMAND [ARG] ...

        Parameters:
            SUBCOMMAND                    subcommand
            [ARG] ...                     subcommand arguments

        Subcommands:
            health                        Health related commands
            upgrade                       Upgrade related commands
            advanced                      Advanced tools for server
                                          maintenance

        Options:
            -h, --help                    print help

    @since: 16.March.2018
    """
    command_base = None  # each inherited instance should define this
    command_sub = None  # specific to instance, like: health, upgrade, etc

    @classmethod
    def _construct_command(cls, options=None):
        """Build a foreman-maintain command based on the options passed"""
        tail = u''

        for key, val in options.items():
            if val is None:
                continue
            if val is True:
                tail += u' --{0}'.format(key)
            elif val is not False:
                if isinstance(val, list):
                    val = ','.join(str(el) for el in val)
                tail += u' --{0}="{1}"'.format(key, val)

        cmd = u'./foreman_maintain/bin/foreman-maintain {0} {1} {2}'.format(
            cls.command_base,
            cls.command_sub,
            tail.strip()
        )
        return cmd

    @classmethod
    def check(cls, options=None):
        """Build foreman-maintain health check"""
        cls.command_sub = 'check'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def list(cls, options=None):
        """Build foreman-maintain health list"""
        cls.command_sub = 'list'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def list_tags(cls, options=None):
        """Build foreman-maintain health list"""
        cls.command_sub = 'list-tags'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def list_versions(cls, options=None):
        """Build foreman-maintain upgrade list-versions"""
        cls.command_sub = 'list-versions'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def run_katello_service_restart(cls, options=None):
        """Build foreman-maintain advanced procedure run
         katello-service-restart"""

        cls.command_sub = 'katello-service-restart'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def run_katello_service_stop(cls, options=None):
        """Build foreman-maintain advanced procedure run
         katello-service-stop"""

        cls.command_sub = 'katello-service-stop'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result

    @classmethod
    def run_katello_service_start(cls, options=None):
        """Build foreman-maintain advanced procedure run
         katello-service-start"""

        cls.command_sub = 'katello-service-start'

        if options is None:
            options = {}

        result = cls._construct_command(options)

        return result
