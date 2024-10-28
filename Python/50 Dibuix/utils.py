import re
import subprocess
from IPython.display import display, Markdown

def show_code(file_path, function_name=None):
    """
    Mostra el codi font d'un fitxer Python complet o d'una funció específica.
    
    Args:
        file_path (str): Ruta al fitxer Python
        function_name (str, optional): Nom de la funció a mostrar. Si és None, 
                                     es mostra tot el fitxer.
    
    Returns:
        None: Mostra el codi formatat utilitzant IPython.display
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            content = ''.join(lines)
        
        if function_name:
            # Troba la línia on comença la funció
            func_pattern = rf"^[ \t]*def[ \t]+{re.escape(function_name)}[ \t]*\("
            start_line = None
            base_indent = None
            func_lines = []
            
            # Primer busquem decoradors
            for i, line in enumerate(lines):
                if line.strip().startswith('@'):
                    if i + 1 < len(lines) and re.match(func_pattern, lines[i + 1], re.MULTILINE):
                        start_line = i
                        base_indent = len(line) - len(line.lstrip())
                        break
                elif re.match(func_pattern, line, re.MULTILINE):
                    start_line = i
                    base_indent = len(line) - len(line.lstrip())
                    break
            
            if start_line is not None:
                # Afegim els decoradors i la definició de la funció
                current_line = start_line
                while current_line < len(lines):
                    line = lines[current_line]
                    if not line.strip():  # Línia en blanc
                        func_lines.append(line)
                        current_line += 1
                        continue
                        
                    indent = len(line) - len(line.lstrip())
                    # Si trobem una línia amb menys indentació que la base, hem sortit de la funció
                    if line.strip() and indent <= base_indent and current_line > start_line and not line.strip().startswith('@'):
                        break
                        
                    func_lines.append(line)
                    current_line += 1
                
                if func_lines:
                    content = ''.join(func_lines)
                else:
                    content = f"# Funció '{function_name}' no trobada al fitxer {file_path}"
            else:
                content = f"# Funció '{function_name}' no trobada al fitxer {file_path}"
        
        # Elimina espais en blanc extra al principi i final
        content = content.rstrip()
        
        # Mostra el codi formatat
        display(Markdown(f'```python\n{content}\n```'))
        
    except FileNotFoundError:
        print(f"Error: No s'ha trobat el fitxer '{file_path}'")
    except Exception as e:
        print(f"Error inesperat: {str(e)}")


def run_code(file_path):
    subprocess.Popen(['python3', file_path])

def draw_grid(pygame, screen, size):

    font = pygame.font.SysFont(None, 20)
    width, height = screen.get_size()

    grid_color = (100, 100, 100)
    
    for x in range(0, width, size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
        if x % 50 == 0:
            text = font.render(str(x), True, grid_color)
            screen.blit(text, (x, 0))
    
    for y in range(0, height, size):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))
        if y % 50 == 0:
            text = font.render(str(y), True, grid_color)
            screen.blit(text, (0, y))
