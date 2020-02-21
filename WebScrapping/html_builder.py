"""list of functions used to build an html tree from an html web page string"""
from WebScrapping.html_element import HtmlElement


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
    content = content.strip()
    content_len = content.__len__()
    last_index = 0
    while last_index < content_len:
        try:
            element = HtmlElement()

            open_index = content.index("<", last_index)
            close_index = content.index(">", last_index)

            tag_name = content[open_index+1:close_index]
            if tag_name.startswith("!--"):
                handle_comment(element, tag_name)
                last_index = close_index+1
                childs_list.append(element)
                continue

            if tag_name.__contains__(" "):
                tag_name = set_tag_attributes(element, tag_name)

            element.tag_type = tag_name
            closing_tag = "</"+tag_name+">"

            if content.__contains__(closing_tag):
                closing_tag_index = find_closing_tag(tag_name, content, last_index)
                last_index = closing_tag_index+closing_tag.__len__()
                sub_section = content[close_index+1:closing_tag_index]
            else:
                closing_tag_index = content.index(">", last_index)
                last_index = closing_tag_index+1
                sub_section = content[close_index+1:closing_tag_index]

            sub_section = sub_section.strip()
            if sub_section.startswith("<"):
                sub_trees = build_node_and_childs(sub_section)
                for sub_tree in sub_trees:
                    element.children.append(sub_tree)
                childs_list.append(element)
            else:
                if sub_section.__contains__("<"):
                    open_tag_index = sub_section.index("<")
                    close_tag_index = sub_section.rindex(">")+1

                    start = sub_section[0:open_tag_index]
                    end = sub_section[close_tag_index:]
                    element.content = start+end

                    tags = sub_section[open_tag_index:close_tag_index]
                    sub_trees = build_node_and_childs(tags)
                    for sub_tree in sub_trees:
                        element.children.append(sub_tree)
                else:
                    element.content = sub_section

                childs_list.append(element)

        except ValueError:
            #print(ValueError)
            #print("ValueError for content "+content)
            last_index = content_len

    return childs_list

def set_tag_attributes(node, tag_name_with_attributes):
    """ Set the tag attribites and return the tag name without attributes"""
    split = tag_name_with_attributes.split()
    first = True
    tag_name = ""
    for sub in split:
        if first:
            tag_name = sub
            first = False
        elif sub.__contains__("="):
            sub_split = sub.split("=")
            attribute_name = sub_split[0]
            attribute_value = sub_split[1]
            node.attributes[attribute_name] = attribute_value
    return tag_name

def find_closing_tag(tag_name, content, last_index):
    """finds the tag that closes the opening started at lastindex"""
    start_tag = "<"+tag_name
    start_tag_len = start_tag.__len__()

    closing_tag = "</"+tag_name+">"
    closing_tag_len = closing_tag.__len__()
    closing_tag_index = -1

    position = last_index
    end = content.__len__()-closing_tag_len
    open_tags = 0

    while position <= end:
        try_start = content[position:position+start_tag_len]
        if try_start == start_tag:
            open_tags = open_tags +1
            position = position + start_tag_len
            continue

        try_close = content[position:position+closing_tag_len]
        if try_close == closing_tag:
            open_tags = open_tags - 1
            if open_tags == 0:
                return position

            position = position + closing_tag_len
            continue

        position = position + 1

    return closing_tag_index

def remove_doctype(page):
    """removes the doctype from the html page"""
    return page.replace("<!DOCTYPE html>", "")


def remove_lines(page):
    """removes the lines skip"""
    return page.replace("\n", "")

def handle_comment(element, tag_name):
    """ Builds the element for the particular case of a comment """
    element.tag_type = "!--"
    element.content = tag_name.replace("!--", "").replace("--", "")
