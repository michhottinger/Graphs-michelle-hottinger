def visit(ancestors, starting_node, node, depth, roots):
    has_parents = False
    for parent, child in ancestors:
        if child == node:
            has_parents = True
            visit(ancestors, starting_node, parent, depth + 1, roots)
    if not has_parents and node != starting_node:    
        roots.append((node, depth))
        
def earliest_ancestor(ancestors, starting_node):
    roots = []
    visit(ancestors, starting_node, starting_node, 0, roots)
    best_node = -1
    best_depth = -1
    for node, depth in roots:
        if depth > best_depth or (depth == best_depth and node < best_node):
            best_node = node
            best_depth = depth            
    return best_node

    