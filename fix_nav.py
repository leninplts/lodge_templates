import re

nav_map = {
    'Inicio': 'index.html',
    'Nosotros': 'nosotros.html',
    'Cómo Llegar': 'como-llegar.html',
    'Habitaciones': 'habitaciones.html',
    'Alimentación': 'alimentacion.html',
    'Actividades': 'actividades.html',
    'Paquetes': 'paquetes.html',
}

footer_nav_map = {
    'Gastronomía': 'alimentacion.html',
    'Experiencias': 'actividades.html',
    'Sostenibilidad': 'nosotros.html',
    'Nuestras Habitaciones': 'habitaciones.html',
}

internal_links = {
    'Ver detalles': 'habitaciones.html',
    'Ver menú': 'alimentacion.html',
    'Explorar tours': 'actividades.html',
    'Conocer más': 'nosotros.html',
    'Explorar Habitaciones': 'habitaciones.html',
}

mobile_menu = """
<button class="lg:hidden p-2" onclick="document.getElementById('mobile-menu').classList.toggle('hidden')">
<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
</button>
</div></div></nav>
<div id="mobile-menu" class="hidden lg:hidden fixed top-[72px] left-0 right-0 z-50 bg-white border-t border-gray-100 px-6 py-4 shadow-lg">
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="index.html">Inicio</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="nosotros.html">Nosotros</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="como-llegar.html">Cómo Llegar</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="habitaciones.html">Habitaciones</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="alimentacion.html">Alimentación</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="actividades.html">Actividades</a>
<a class="block py-3 text-gray-600 hover:text-primary transition-colors" href="paquetes.html">Paquetes</a>
<a class="block py-3 bg-primary text-white text-center rounded-lg font-semibold mt-2" href="https://api.whatsapp.com/send?phone=51987654321">Reservar</a>
</div>
"""

def fix_file(src, dst, active_page):
    with open(src, 'r') as f:
        content = f.read()
    
    for text, href in nav_map.items():
        pattern = rf'(href="#")(>\s*{re.escape(text)}\s*<)'
        replacement = rf'href="{href}"\2'
        content = re.sub(pattern, replacement, content)
    
    for text, href in {**footer_nav_map, **nav_map}.items():
        pattern = rf'(href="#")(>{re.escape(text)}<)'
        replacement = rf'href="{href}"\2'
        content = re.sub(pattern, replacement, content)
    
    for text, href in internal_links.items():
        pattern = rf'(href="#")(>[^<]*{re.escape(text)})'
        replacement = rf'href="{href}"\2'
        content = re.sub(pattern, replacement, content)
    
    if 'mobile-menu' not in content:
        content = content.replace('</nav>', mobile_menu, 1)
    
    with open(dst, 'w') as f:
        f.write(content)
    
    print(f"Fixed: {src} -> {dst} (active: {active_page})")

files = {
    ('/tmp/stitch_index.html', '/Users/lenin/Desktop/allfiles/lyr/crm/index.html', 'Inicio'),
    ('/tmp/stitch_nosotros.html', '/Users/lenin/Desktop/allfiles/lyr/crm/nosotros.html', 'Nosotros'),
    ('/tmp/stitch_comollegar.html', '/Users/lenin/Desktop/allfiles/lyr/crm/como-llegar.html', 'Cómo Llegar'),
    ('/tmp/stitch_habitaciones.html', '/Users/lenin/Desktop/allfiles/lyr/crm/habitaciones.html', 'Habitaciones'),
    ('/tmp/stitch_alimentacion.html', '/Users/lenin/Desktop/allfiles/lyr/crm/alimentacion.html', 'Alimentación'),
    ('/tmp/stitch_actividades.html', '/Users/lenin/Desktop/allfiles/lyr/crm/actividades.html', 'Actividades'),
    ('/tmp/stitch_paquetes.html', '/Users/lenin/Desktop/allfiles/lyr/crm/paquetes.html', 'Paquetes'),
}

for src, dst, active in files:
    fix_file(src, dst, active)

print("All files processed!")
