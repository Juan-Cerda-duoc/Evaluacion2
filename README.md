# Evaluacion2 - Planificador de Rutas con Graphhopper

Este proyecto es un script Python para calcular rutas de viajes utilizando graphhopper media un API entregada por la pagina web respectiva.. Permite ingresar un punto de partida y un destino desde la consola para obtener las indicaciones paso a paso de forma rápida y clara.



Como funciona: 

- Multilingüe: Puedes usarlo en Español o Inglés. Para ello solo deberás elegir el idioma que más se te acomode para usar el script de una forma más cómoda. Toda la interfaz y las instrucciones de las calles se adaptan al idioma que elijas. 
- Narrativa a tu ritmo : Las narrativas del viaje se imprimen con un tiempo de 2 segundos para que las instrucciones puedan ser leidas con calma evitando que se sature toda la terminal imprimiendo todo la información sobre la ruta de golpe. 
- Números claros: Las distancias (en kilómetros y millas) están redondeadas a un máximo de 2 decimales.
- Diferentes medios de transporte: Puedes consultar rutas para auto, bicicleta o caminar.
- Salida sencilla: Si quieres cerrar el programa en cualquier momento, basta con escribir s o salir (o q / quit si elegiste inglés).



Requisitos

Solo necesitas tener instalado Python 3 y la librería requests:

```bash
pip install requests
```



Cómo se usa

1. Descarga o clona este repositorio:
   ```bash
   git clone [https://github.com/Juan-Cerda-duoc/Evaluacion2.git](https://github.com/Juan-Cerda-duoc/Evaluacion2.git)
   cd Evaluacion2
   ```

2. Ejecuta el archivo principal:
   ```bash
   python granhopper.py
   ```

3. Sigue las instrucciones en pantalla:
   - Selecciona tu idioma preferido.
   - Elige cómo te vas a desplazar (auto, bicicleta o pie).
   - Escribe el lugar de origen y de destino (Con el siguiente formato: Calle y numeracion, comuna, Pais Ej: Antonio Varas 666, providencia, Chile).
   - Observa la narrativa del viaje en pantalla.



Archivos del proyecto

- granhopper.py: Código principal en Python.
- README.md: Guía de uso del proyecto.