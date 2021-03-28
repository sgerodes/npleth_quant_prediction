from nplet import Nplet
#from exceptions import NodeInitException


class Nplet_node():
    rising_key = 1
    falling_key = 0

    def __init__(self, nplet):
        #check_type_nplet(nplet_key)
        self.nplet = nplet
        self.accessors = {}
        self.triggered = 0

    def set_rising_accessor(self, nplet_node):
        #check_type_nplet_node(nplet_node)
        self.accessors[Nplet_node.rising_key] = nplet_node

    def set_falling_accessor(self, nplet_node):
        #check_type_nplet_node(nplet_node)
        self.accessors[Nplet_node.falling_key] = nplet_node

    def inc_rising_count(self):
        self.inc_triggered()
        self.nplet.inc_rising_count()

    def inc_falling_count(self):
        self.inc_triggered()
        self.nplet.inc_falling_count()

    def inc_triggered(self):
        self.triggered += 1

    def has_both_accessors(self):
        return len(self.accessors) == 2

    def get_rising_accessor(self):
        return self.accessors[Nplet_node.rising_key]

    def get_falling_accessor(self):
        return self.accessors[Nplet_node.falling_key]

    def get_nplet(self):
        return self.nplet

    def get_key(self):
        return self.get_nplet().get_key()

    def get_triggered(self):
        return self.triggered

    def __repr__(self):
        return 'Nplet_node(key=\'{}\', triggered={}, nplet={})'.format(self.get_key(),
                                                                            self.triggered,
                                                                              self.get_nplet())


# def check_type_nplet(nplet):
#     if not isinstance(nplet, Nplet):
#         raise NodeInitException("Expected type {}, but was {}".format(Nplet, type(nplet)))
#
#
# def check_type_nplet_node(nplet_node):
#     if not isinstance(nplet_node, Nplet_node):
#         raise NodeInitException("Expected type {}, but was {}".format(Nplet_node, type(nplet_node)))
