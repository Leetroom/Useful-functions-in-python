html_dom = {
    'html': {
        'head': {
            'title': 'Arasaka',
        },
        'body': {
            'h2': 'Hello!',
            'div': 'If you wont, i can tail this story?...',
            'p': 'The end.',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result


res = find_element(tree=html_dom, element_name='title')
print(res)