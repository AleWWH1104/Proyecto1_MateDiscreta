def parse_nested_lists(s, reference_set):
    def parse(s):
        stack = []
        current_list = []
        current_str = ''
        i = 0
        while i < len(s):
            char = s[i]
            if char == '(':
                # Push current list onto stack and start new list
                stack.append(current_list)
                current_list = []
                i += 1
            elif char == ')':
                # End current list and pop from stack
                if current_str:
                    current_list.append(current_str.strip())
                    current_str = ''
                top_list = stack.pop()
                top_list.append(current_list)
                current_list = top_list
                i += 1
            elif char == ',':
                if current_str:
                    current_list.append(current_str.strip())
                    current_str = ''
                i += 1
            else:
                current_str += char
                i += 1
        
        if current_str:
            current_list.append(current_str.strip())
        
        return current_list
    
    def validate_elements(lst):
        """Valida que todos los elementos de la lista estén en reference_set."""
        if isinstance(lst, list):
            for elem in lst:
                if isinstance(elem, list):
                    if not validate_elements(elem):
                        return False
                elif elem not in reference_set:
                    return False
            return True
        else:
            return lst in reference_set

    s = s.replace(' ', '')  # Eliminar espacios
    nested_list = parse(s)
    
    if validate_elements(nested_list):
        return nested_list
    else:
        raise ValueError("Error: Un elemento no pertenece al conjunto referencial.")

# Conjunto referencial de ejemplo
reference_set = {'a', 'b', 'c', 'd', 'e', 'f'}

# Ejemplo de uso
s = "(a,b,(c,d,(e,f)),g)"
try:
    result = parse_nested_lists(s, reference_set)
    print(result)
except ValueError as e:
    print(e)
