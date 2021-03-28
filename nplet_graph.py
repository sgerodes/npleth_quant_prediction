# Binary directed circular complete Graph. Where every node contains one nplet
from itertools import product
from nplet_node import Nplet_node
from nplet import Nplet

class Nplet_graph():
    rising_key = "1"
    falling_key = "0"

    def __init__(self, N):
        self.N = N
        self.nodes = {}
        self._initialize_graph()
        self.current = None
        self.triggered = 0.0

    def move_rising(self):
        self.current.inc_rising_count()
        self.current = self.current.get_rising_accessor()

    def move_falling(self):
        self.current.inc_falling_count()
        self.current = self.current.get_falling_accessor()

    def add_value(self, delta_to_prev):
        self.triggered += 1
        if delta_to_prev > 0:
            self.move_rising()
        else:
            self.move_falling()

    def _add_node(self, nplet_key, nplet_node):
        self.nodes[nplet_key] = nplet_node


    def set_current(self, nplet_key=None):
        if nplet_key is None:
            nplet_key = Nplet_graph.falling_key*N
        self.current = self.nodes[nplet_key]

    def get_current(self):
        return self.current

    def _initialize_graph(self):
        self._create_nodes()
        self._link_nodes()

    def _create_nodes(self):
        for nplet_key_tuple in product(Nplet_graph.rising_key + Nplet_graph.falling_key, repeat=self.N):
            key = ''.join(nplet_key_tuple)
            node = Nplet_node(Nplet(key))
            self._add_node(key, node)

    def _link_nodes(self):
        for node in self.nodes.values():
            key = node.get_key()
            node.set_rising_accessor(self.nodes[Nplet_graph.create_next_rising_key(key)])
            node.set_falling_accessor(self.nodes[Nplet_graph.create_next_falling_key(key)])

    def __repr__(self):
        return 'Nplet_graph(node_count={}; graph_triggered={} current={}\n {}\n)'\
            .format(len(self.nodes),
                    self.triggered,
                    str(self.current),
                    ';\n '.join([ '{}; frequency={}'.format( str(node), node.triggered/self.triggered * len(self.nodes) if node.triggered > 0 else 0,) for node in self.nodes.values()]))

    @staticmethod
    def create_next_rising_key(prev):
        return (prev + Nplet_graph.rising_key)[1:]

    @staticmethod
    def create_next_falling_key(prev):
        return (prev + Nplet_graph.falling_key)[1:]


if __name__ == '__main__':
    N = 2
    graph = Nplet_graph(N)
    graph.set_current()
    print(graph)
    graph.add_value(123)
    print (graph)
    graph.add_value(123)
    print (graph)
    graph.add_value(-23)
    print (graph)