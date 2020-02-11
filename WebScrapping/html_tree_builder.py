"""list of functions used to build an html tree from an html web page string"""
import html_tree


def build_html_tree(page):
    """creates a tree from an html string page"""
    # first string preparation
    page = page.strip()
    page = remove_doctype(page)
    page = remove_lines(page)
    tree = build_node_and_childs(page)
    return tree[0]


def build_node_and_childs(content):
    """recursively creates a nodes from an htmlstring page"""
    if not content.__contains__("<"):
        return None

    childs_list = []
    content_len = content.__len__()
    last_index = 0
    while last_index < content_len:
        open_index = content.index("<", last_index)
        close_index = content.index(">", last_index)

        tag_name = content[open_index+1:close_index]

        closing_tag = "</"+tag_name+">"
        closing_tag_index = content.index(closing_tag, last_index)
        last_index = closing_tag_index+closing_tag.__len__()
        sub_section = content[close_index+1:closing_tag_index]

        if not sub_section.__contains__("<"):
            tree = html_tree.HtmlTree(tag_name, sub_section)
            childs_list.append(tree)
        else:
            tree = html_tree.HtmlTree(tag_name, "")
            sub_trees = build_node_and_childs(sub_section)
            for sub_tree in sub_trees:
                tree.children.append(sub_tree)
            childs_list.append(tree)

    return childs_list


def remove_doctype(page):
    """removes the doctype from the html page"""
    return page.replace("<!DOCTYPE html>", "")


def remove_lines(page):
    """removes the lines skip"""
    return page.replace("\n", "")
