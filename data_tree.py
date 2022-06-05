from random import randint


class Tree_Node:
    def __init__(self, data, side, level):
        self.data = data
        self.child_left = None
        self.child_right = None
        self.parent = None
        self.side =  side
        self.level = level
    
    def add_children(self, child, side):
        child.parent = self
        if side == 0:
            self.child_left = child
        if side == 1:
            self.child_right = child

    def print_tree(self):
        spaces = '-' * self.level*3 + '|'*bool(self.level)
        side = ""
        if self.side == 0:
            side = "left"
        if self.side == 1:
            side = "right"

        if self.data != 0:
            print(spaces, side, self.data)
            if self.child_left:
                self.child_left.print_tree()
                self.child_right.print_tree()

def side_data_value(min_value, max_value):
    if max_value - min_value >= 0 and min_value != 0 and max_value != 0:
        if max_value - min_value > 1 and max_value - min_value <= 9:
            return randint(min_value, max_value)
        else:
            return randint(min_value, min_value+9)
    else:
        return 0


def build_data_tree():
    base = 100
    root = Tree_Node(base, None, 0)

    #left side 1 level
    base_11 = side_data_value(base-10, base-1)
    #testing line
    #base_1 = 99
    child_11 = Tree_Node(base_11, 0, 1)

    #left side 2 level
    base_21 = side_data_value(base_11-10, base_11-1)
    child_21 = Tree_Node(base_21, 0, 2)
    base_22 = side_data_value(base_11+1, base-1)
    child_22 = Tree_Node(base_22, 1, 2)

    #left side 3 level from 21
    child_31 = Tree_Node(side_data_value(base_21-10, base_21-1), 0, 3)
    child_32 = Tree_Node(side_data_value(base_21+1, base_11-1), 1, 3)

    #left side 3 level from 22
    child_33 = Tree_Node(side_data_value(base_11 + 1, base_22-1), 0, 3)
    child_34 = Tree_Node(side_data_value(base_22+1, base-1), 1, 3)

    #right side 1 level
    base_12 = side_data_value(base + 1, base + 10)
    #testing line
    #base_1 = 101
    child_12 = Tree_Node(base_12, 1, 1)

    #left side 2 level
    base_23 = side_data_value(base + 1, base_12-1)
    child_23 = Tree_Node(base_23, 0, 2)
    base_24 = side_data_value(base_12+1, base_12 + 10)
    child_24 = Tree_Node(base_24, 1, 2)

    #right side 3 level from 23
    child_35 = Tree_Node(side_data_value(base+1, base_23-1), 0, 3)
    child_36 = Tree_Node(side_data_value(base_23+1, base_12-1), 1, 3)

    #right side 3 lever from 24
    child_37 = Tree_Node(side_data_value(base_12+1, base_24-1), 0, 3)
    child_38 = Tree_Node(side_data_value(base_24+1, base_24+10), 1, 3)

    #adding first level children
    root.add_children(child_11, 0)
    root.add_children(child_12, 1)

    #adding second level children
    child_11.add_children(child_21, 0)
    child_11.add_children(child_22, 1)
    child_12.add_children(child_23, 0)
    child_12.add_children(child_24, 1)

    #adding third level children
    child_21.add_children(child_31, 0)
    child_21.add_children(child_32, 1)
    child_22.add_children(child_33, 0)
    child_22.add_children(child_34, 1)
    child_23.add_children(child_35, 0)
    child_23.add_children(child_36, 1)
    child_24.add_children(child_37, 0)
    child_24.add_children(child_38, 1)

    return root

if __name__ == '__main__':
    root = build_data_tree()
    root.print_tree()
    pass

