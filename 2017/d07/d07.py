import re
from collections import defaultdict


test_input = [
    'pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)'
]

check_children_pattern = '.*->.*'
node_with_children_pattern = '^(\w+) \((\d+)\)(?: -> )?(.*)$'
node_without_children_pattern = '^(\w+) \((\d+)\)$'


class Node:
    name = ''
    parent = None
    children = []
    node_weight = 0

    def __init__(self, name, parent, children, node_weight):
        self.name = name
        self.parent = parent
        self.children = frozenset(children)
        self.node_weight = node_weight


    def getParent(self):
        return self.parent


    def getChildren(self):
        return self.children


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def createNode(regex_node_line, with_children):
    if with_children:
        name = regex_node_line.group(1)
        children = regex_node_line.group(3).split(', ')
        node_weight = int(regex_node_line.group(2))
        node = Node(name, None, children, node_weight)
    else:
        name = regex_node_line.group(1)
        node_weight = regex_node_line.group(2)
        node = Node(name, None, [], node_weight)
    return node



def createProgramTree(input_data):
    program_tree = defaultdict()
    for node_line in input_data:
        if re.match(check_children_pattern, node_line):
            regex_node_line = re.search(node_with_children_pattern, node_line)
            node = createNode(regex_node_line, True)
            program_tree.update({node.name: node})
        else:
            regex_node_line = re.search(node_without_children_pattern, node_line)
            node = createNode(regex_node_line, False)
            program_tree.update({node.name: node})
    return program_tree


def putParentIntoNodes(program_tree):
    for tree_element in program_tree.keys():
        children_in_node = program_tree.get(tree_element).children
        for child_name in children_in_node:
            child_in_program_tree = program_tree.get(child_name)
            child_in_program_tree.parent = tree_element


def giveMeThisShit(program_tree):
    for tree_element in program_tree.keys():
        if program_tree.get(tree_element).parent is None:
            return tree_element


def getBottomProgram(input_data):
    program_tree = createProgramTree(input_data)
    putParentIntoNodes(program_tree)
    name_of_bottom_program_node = giveMeThisShit(program_tree)
    return name_of_bottom_program_node


def test():
    assert getBottomProgram(test_input) == 'tknk'


def main():
    test()
    input_data = readInputFile()
    print('Day 7 Part 1:', getBottomProgram(input_data))


if __name__ == '__main__':
    main()
