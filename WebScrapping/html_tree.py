"""Class that models an html document as a tree"""


class HtmlTree:
    """Class that models an html document as a tree"""
    def __init__(self, tag_type, content):
        self.tag_type = tag_type
        self.content = content
        self.children = []

    def depth(self):
        """Compute the depth of the tree"""
        if self.children is None:
            return 1

        max_depth = 0
        for child in self.children:
            if child is None:
                return 1
            child_depth = child.depth()
            if child_depth > max_depth:
                max_depth = child_depth

        return max_depth+1

    def count_nodes(self):
        """Counts the number of tags of the tree"""
        if self.children is None:
            return 0

        total_count = 0
        for child in self.children:
            if child is None:
                return 0
            child_count = child.count_nodes()
            total_count = total_count + child_count

        return total_count+1

    def get_element_by_tag_type(self, tag_type):
        """Returns all the elements that matches the type """
        elts = []
        if self is None:
            return elts
        if self.tag_type == tag_type:
            elts.append(self)

        for child in self.children:
            if child is None:
                continue
            sub_elts = child.get_element_by_tag_type(tag_type)
            if sub_elts is not None:
                for sub_elt in sub_elts:
                    elts.append(sub_elt)

        return elts
